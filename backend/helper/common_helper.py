import datetime
from enum import Enum

import pytz
from threading import Lock
from django.db import connections

from backend.helper.logging_helper import Logger

logger = Logger(__name__)


class Singleton(type):
    "Singleton class based on singleton design pattern"
    _instances = {}
    _lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super(Singleton, cls).__call__(
                    *args, **kwargs
                )
        return cls._instances[cls]


def check_mysql_connection():
    # checking the slave connection for our use case
    conn = connections["slave"]

    # Check if the connection is alive
    try:
        conn.ensure_connection()
        return True
    except Exception:
        return False


class ObjectEnum(Enum):
    def __eq__(self, other):
        """compares with or value of enum without explicit mention"""
        if isinstance(other, ObjectEnum):
            return self.value == other.value
        elif isinstance(other, type(self.value)):
            return self.value == other
        return False

    def __str__(self):
        return self.value

    @classmethod
    def list_values(cls):
        return [i for i in cls.__members__.values()]

    @classmethod
    def list_keys(cls):
        return [i for i in cls.__members__.keys()]

    @classmethod
    def from_value(cls, value, strict=True):
        """
        returns first value matched found in iterator
        Careful: if enum has duplicate values
        :param value: to be compared in enum
        :param strict: if True raises Exception if value not found
        :return:
        :raises InvalidValueException if value doesn't exists and strict
        """
        for _, v in cls.__members__.items():
            if v == value:
                return v
        if strict:
            raise ValueError("{} not a valid choice".format(value))


def convert_utc_date_to_ist_epoch(date_stamp):
    """Convert UTC ->  EPOCH"""

    if not date_stamp:
        logger.log_error("Incorrect date_stamp {}".format(date_stamp))
        return None

    if isinstance(date_stamp, str):
        if len(date_stamp) == 10:
            date_stamp = datetime.datetime.strptime(date_stamp, "%Y-%m-%d")
        else:
            date_stamp = datetime.datetime.strptime(
                date_stamp[:19], "%Y-%m-%d %H:%M:%S"
            )

    elif isinstance(date_stamp, datetime.date):
        date_stamp = date_stamp.strftime("%Y-%m-%d %H:%M:%S")
        date_stamp = datetime.datetime.strptime(
            date_stamp, "%Y-%m-%d %H:%M:%S"
        )
    tz = pytz.timezone("Asia/Kolkata")
    local_time = tz.localize(date_stamp)

    return local_time.timestamp()
