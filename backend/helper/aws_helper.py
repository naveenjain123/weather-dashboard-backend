import csv
import io
import os
import traceback
from functools import partial

import boto3
import numpy as np
import pandas as pd
from botocore.exceptions import ClientError

from backend import settings
from backend.helper.logging_helper import Logger

logger = Logger(__name__)
DEBUG = os.getenv("DEBUG", False)


def get_boto_client_partial():
    client = partial(
        boto3.session.Session().client,
        aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
        aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY,
    )
    return client


class S3(object):
    _instance = None

    """
        this class is for aws s3 related activities
    """

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(S3, cls).__new__(cls)
            try:
                boto_client = get_boto_client_partial()
                cls.client = boto_client("s3")

            except Exception as e:
                raise e
        return cls._instance

    @classmethod
    def upload_file_to_S3_bucket(
        cls, key, file_data, file_type="binary", expiresIn=None, headers=None
    ):
        """
        this method is for upoading the file to S3 bucket
        Accepts: upload_obj,headers
        Returns: returns filename of the file uploaded if succesfully
        """
        bucket_name = settings.S3_BUCKET
        extraArgs = {"ACL": "public-read"}
        if expiresIn is not None:
            extraArgs["Expires"] = expiresIn

        try:
            if file_type == "binary":
                # Transform the binary data into something
                # which can be used like a file handle
                file_buff = io.BytesIO()
                file_buff.write(file_data)

                file_buff.seek(0)

                # Upload in-memory object to S3 bucket
                try:
                    cls.client.upload_fileobj(
                        Fileobj=file_buff,
                        Bucket=settings.S3_BUCKET,
                        Key=key,
                        ExtraArgs=extraArgs,
                        Callback=None,
                        Config=None,
                    )
                except ClientError:
                    logger.log_error(
                        "Error while uploading image to s3 = {}".format(
                            traceback.format_exc()
                        )
                    )
            elif file_type == "csv":
                if len(file_data) > 0:
                    stream = io.StringIO()

                    writer = csv.DictWriter(stream, fieldnames=headers)
                    writer.writeheader()
                    writer.writerows(file_data)

                    csv_string_object = stream.getvalue()
                    logger.log_info(
                        "Uploading Object {}".format(csv_string_object)
                    )
                    cls.client.put_object(
                        Bucket=bucket_name,
                        Key=key,
                        Body=csv_string_object,
                        ACL="public-read",
                        Expires=expiresIn,
                    )
            else:
                # uploading other type of file with put_object method

                cls.client.put_object(
                    Bucket=bucket_name, Key=key, Body=file_data
                )

            object_url = "https://{}.s3.{}.amazonaws.com/{}".format(
                settings.S3_BUCKET, settings.S3_REGION_NAME, key
            )
            return object_url
        except Exception as e:
            logger.log_warning("Exception Uploading File to S3: {}".format(e))
            logger.log_error("Traceback = {}".format(traceback.format_exc()))
            raise e

    @classmethod
    def get_presigned_url(cls, object_key):
        """
        this method is for fetching the presigned url for an object in s3 bucket
        Accepts: object_key
        Returns: returns presigned url
        """
        bucket_name = settings.S3_BUCKET

        try:
            url = cls.client.generate_presigned_url(
                ClientMethod="put_object",
                Params={"Bucket": bucket_name, "Key": object_key},
                ExpiresIn=settings.S3_EXPIRE_TIME,
            )

        except ClientError as e:
            logger.log_warning(
                "Exception while fetching presigned url File to S3: {}".format(
                    e
                )
            )
            logger.log_error("Traceback = {}".format(traceback.format_exc()))
            raise e

        return url

    @classmethod
    def read_csv_contents(cls, object_key):
        """
        this method is for rrading the csv file from s3 bucket
        Accepts: object_key
        Returns: returns the csv_headers->list of the csv headers
                 csvreader-> csv rreader list object though which we can iterate to fetch data
        """
        bucket_name = settings.S3_BUCKET

        try:
            csv_file_obj = cls.client.get_object(
                Bucket=bucket_name, Key=object_key
            )
        except ClientError as e:
            logger.log_warning(
                "Exception while downloading the file csv from s3 {}".format(e)
            )
            logger.log_error("Traceback = {}".format(traceback.format_exc()))
            raise e
        df = pd.read_csv(csv_file_obj["Body"])
        csv_headers = list(df.columns)

        # replacing empty values with '-'
        empty = "-"
        df.fillna(empty)
        df.replace(np.nan, empty, inplace=True)
        df.drop_duplicates(inplace=True, keep="first")

        csvreader = df.to_dict(orient="records")
        logger.log_info("CSV File = {}".format(csvreader))

        return csv_headers, csvreader
