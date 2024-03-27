# Common Function
import math

from django.conf import settings
from rest_framework.exceptions import NotFound


class PaginationHelper:
    def __init__(self, *args, **kwargs):
        self.request = kwargs.get("request")

    def paginate(self, total_records, page_number, page_size=10, **kwargs):
        """
        :param total_records:
        :param page_size:
        :param page_number:
        :param total_page: total record of the rows
        :param kwargs: pass variable keyword argument
        :return: dictionary of data that is used in pagination
        """

        start = (page_number - 1) * page_size
        end = start + page_size

        if page_number > math.ceil(total_records / page_size):
            raise NotFound({"status": "error", "message": "Page Not Found"})

        pagination_format = {
            "total_records": total_records,
            "total_page": math.ceil(total_records / page_size),
            "current_page": page_number,
        }
        return pagination_format
