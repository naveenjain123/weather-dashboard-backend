import os

from backend.apps.dashboard.models.search_report_model import SearchReport
from backend.helper.logging_helper import Logger

# from backend.settings.base import *

logger = Logger(__name__)

class WeatherHistoryDao:
    def __init__(self, params, *args, **kwargs):
        domain = params.get("domain", "").split(".")[0]
        query = "SELECT  t.id,MAX(t.id),t.title,t.url, d.old_domain_name, d.id as did from trending_search t join domain d on (t.domain_id=d.id) where status='Published' {sub_query} GROUP BY t.weight;"
        if domain:
            domain = domain + ".careers360.com"
            sub_query = f'AND t.domain_id in (Select id from domain where old_domain_name="{domain}")'

        else:
            sub_query = ""
        self.query = query.format(sub_query=sub_query)

    # function to add search report
    def fetch_popular_search_results(self):
        """
        The function fetches the most popular search results from a database table called
        "trending_search" and returns them.
        :return: the popular search results from the database.
        """
        try:
            popular_search_results = SearchReport.objects.raw(self.query)
            return popular_search_results

        except Exception as e:
            logger.log_error(
                "Error in fetch_popular_search_results {}".format(str(e))
            )
            return []