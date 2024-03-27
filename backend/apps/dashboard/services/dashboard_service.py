from backend.apps.dashboard.dao import (
    WeatherHistoryDao,
)
from backend.helper.logging_helper import Logger

logger = Logger(__name__)

class WeatherHistoryService:
    def __init__(self, params, *args, **kwargs):
        self.weather_history_dao = WeatherHistoryDao(params)

    def get_weather_history_results(self):
        """
        The get_weather_history_results function returns a list of weather history results.

        :param self: Represent the instance of the class
        :return: A dictionary with a key of results and value of weather_history_results
        """
        data = self.weather_history_dao.fetch_popular_search_results()
        weather_history_results = [
            {
                
            }
            for weather_history_record in data
        ]
        response = {"results": weather_history_results}
        return response