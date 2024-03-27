from abc import ABC, abstractmethod

import requests

from backend.helper.logging_helper import Logger

logger = Logger(__name__)


class HttpUtility(ABC):
    """Abstract base class for http related external service calls."""

    def __init__(self):
        pass

    @abstractmethod
    def get_headers(cls, **kwargs):
        """Abstract method to get the headers"""
        """
        return headers required for accessing http APIs
        :return:
        """
        raise NotImplementedError("Subclasses must implement this method")

    @classmethod
    def call_api(cls, method, endpoint, payload, **kwargs):
        """
        kwargs  can contain:
            - headers
            - extra_headers
            - no_of_retries
            - response_code for retries: List[Numbers]
            - timeout: in seconds, default 10 seconds

        :param method:
        :param endpoint:
        :param payload:
        :param kwargs:
        :return:
        """
        resp = dict()
        headers = cls.get_headers(**kwargs)
        codes_to_retry = []
        retry = kwargs.get("retry", 1)
        if "response_codes_to_retry" in kwargs:
            codes_to_retry = kwargs["response_codes_to_retry"]
        while retry > 0 and (resp == {} or resp.status_code in codes_to_retry):
            if method == "GET":
                headers.pop(
                    "Content-Type"
                )  # Content-Type: application/json will give error in GET request
                payload = payload or {}
                resp = requests.get(
                    url=endpoint,
                    headers=headers,
                    params=payload,
                    timeout=kwargs.get("timeout", 10),
                )
            elif method == "POST":
                resp = requests.post(
                    url=endpoint,
                    headers=headers,
                    data=payload,
                    timeout=kwargs.get("timeout", 10),
                )
            elif method == "PUT":
                resp = requests.put(
                    url=endpoint,
                    headers=headers,
                    data=payload,
                    timeout=kwargs.get("timeout", 10),
                )
            elif method == "DELETE":
                resp = requests.delete(
                    url=endpoint,
                    headers=headers,
                    data=payload,
                    timeout=kwargs.get("timeout", 10),
                )
            else:
                raise NotImplementedError("This method is not implemented")

            retry = retry - 1

        logger.log_info("Response: status_code={}".format(resp.status_code))
        return resp
