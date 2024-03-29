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
        data = self.weather_history_dao.fetch_weather_history_results()
        weather_history_results = [
            {
                "id":weather_history_record.id,
                "country":weather_history_record.country,
                "temp_min":weather_history_record.temp_min,
                "temp_max":weather_history_record.temp_max,
                "pressure":weather_history_record.pressure,
                "humidity":weather_history_record.humidity,
                "date":weather_history_record.date
            }
            for weather_history_record in data
        ]
        response = {"results": weather_history_results}
        return response