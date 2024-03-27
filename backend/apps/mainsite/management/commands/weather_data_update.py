from datetime import datetime
from django.core.management.base import BaseCommand

from backend.helper.logging_helper import Logger

logger = Logger(__name__)


class Command(BaseCommand):
    help = "Insert all the entity_search index documents from here"

    def add_arguments(self, parser):
        parser.add_argument(
            "-c",
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
            pass
        chunk_size = 500
        limit = 150000

        