import json
from datetime import datetime
from django.core.management.base import BaseCommand
import requests
from backend.apps.dashboard.models.weather_model import WeatherHistory
from backend.helper.logging_helper import Logger

logger = Logger(__name__)


class Command(BaseCommand):
    help = "Insert all the entity_search index documents from here"

    def add_arguments(self, parser):
        parser.add_argument(
            "-w",
            "--weather_data",
            type=str,
            nargs="*",
            help="inserting data from open weather API to weather history table",
        )
        
    def handle(self, *args, **options):
        """
        The above function handles different options to populate data for weather history.
        """
        print(options)
        """
        any commands can be written here for any activity

        """
        if options["weather_data"]:
            chunk_size = 500
            url = "http://api.openweathermap.org/data/2.5/forecast?q=delhi&appid=8696524a86014aefc538bcf238ffe6bb"
            weather_api_history = requests.get(url=url, headers={}, params={}, timeout=10)
        chunk = []
        weather_api_history = (weather_api_history.json())
        print(weather_api_history)
        if len(weather_api_history["list"])>0:
            for weather_record in weather_api_history["list"]:
                weather_history_record = WeatherHistory()
                weather_main_data = weather_record["main"]
                weather_history_record.country = "delhi"
                weather_history_record.temp_min = weather_main_data['temp_min']
                weather_history_record.temp_max = weather_main_data['temp_max']
                weather_history_record.pressure = weather_main_data['pressure']
                weather_history_record.humidity = weather_main_data['humidity']
                weather_history_record.timestamp = weather_record['dt_txt']
                datetime_obj_str = datetime.strptime(weather_record['dt_txt'], 
                                 "%Y-%m-%d  %H:%M:%S")
                weather_history_record.date = datetime_obj_str.date()
                chunk.append(weather_history_record)
                if len(chunk) >= chunk_size:
                    logger.log_info(f"adding till index {chunk[-1]}")
                    WeatherHistory.objects.bulk_create(chunk)
                    chunk = []
                if chunk:
                    WeatherHistory.objects.bulk_create(chunk)


        