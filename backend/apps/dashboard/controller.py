
from django.http import JsonResponse
from rest_framework import status

from rest_framework.views import APIView

from backend.apps.dashboard.services.dashboard_service import (
    WeatherHistoryService,
)
from backend.helper.common_helper import (
    check_mysql_connection
)
from backend.helper.custom_permission import ApiKeyPermission
from backend.helper.logging_helper import Logger
from backend.helper.redis_helper import CachedMixin
from backend.helper.response import SuccessResponse

logger = Logger(__name__)


class ServiceCheckAPI(APIView):
    def get(self, request, format=None):
        """
        The function performs a health check on the MySQL databases and returns a JSON
        response indicating the status of the connections.

        :param request: The `request` parameter is an object that represents the HTTP request made by
        the client. It contains information such as the request method (GET, POST, etc.), headers, query
        parameters, and body data. It is used to retrieve information from the client and to send a
        response back to the client
        :param format: The "format" parameter is used to specify the desired format of the response. It
        can be used to request the response in different formats such as JSON, XML, HTML, etc. If the
        "format" parameter is not provided, the default format specified in the request headers will be
        used
        :return: a JSON response with the context dictionary and an HTTP status code.
        """
        context = {"status": "OK", "detail": "Search Service Health Check API"}

        # checking the mysql db connection is successfull or not
        if not check_mysql_connection():
            context["status"] = "NOT_OK"
            context["detail"] = "Unable to connect with mysql database"
            return JsonResponse(
                context, status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
        # If all checks pass, return a successful response
        return JsonResponse(context, status=status.HTTP_200_OK)

class WeatherHistoryApi(APIView):
    permission_classes = (ApiKeyPermission,)

    def get(self, request, version, format=None):
        """
        The above function retrieves weather history results and returns a success response with the
        results.

        :param request: The `request` parameter is an object that represents the HTTP request made by the
        client. It contains information such as the request method, headers, and query parameters
        :param version: The "version" parameter is used to specify the version of the API that the client
        is requesting. It helps in maintaining backward compatibility and allows for making changes to the
        API without breaking existing clients
        :param format: The `format` parameter is used to specify the desired format of the response. It
        can be used to request the response in different formats such as JSON, XML, or HTML. If the
        `format` parameter is not provided, the default format specified in the request headers will be
        used
        :return: a SuccessResponse object with the weather_history_response as the data, a status code of
        200 (HTTP_200_OK), and direct_results set to True.
        """
        weather_history_service_obj = WeatherHistoryService(request.query_params)
        weather_history_search_response = (
            weather_history_service_obj.get_weather_history_results()
        )
        return SuccessResponse(
            weather_history_search_response,
            status=status.HTTP_200_OK,
            direct_results=True,
        )