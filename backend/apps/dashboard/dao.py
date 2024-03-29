import os

from backend.apps.dashboard.models.weather_model import WeatherHistory
from backend.helper.logging_helper import Logger

logger = Logger(__name__)

class WeatherHistoryDao:
    def __init__(self, params, *args, **kwargs):
        from_date = params.get("from_date")
        to_date = params.get("to_date")
        query = "SELECT 1 as id,max(temp_max) as temp_max,min(temp_min) as temp_min,max(humidity) as humidity,date from weather_history as wh  where wh.date>= {} group by wh.date".format(from_date,to_date)
        self.query = query

    # function to fetch weather history results
    def fetch_weather_history_results(self):
        """
        The function fetches the weather history data from a database table called
        "weather_history" according to the dates passed.
        :return: the weather history data from the database.
        """
        try:
            weather_history_data = WeatherHistory.objects.raw(self.query)
            return weather_history_data

        except Exception as e:
            logger.log_error(
                "Error in fetch_weather_history_results {}".format(str(e))
            )
            return []