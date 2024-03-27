"""search report model"""
from datetime import datetime
from django.utils import timezone

from django.db import models


class SearchReport(models.Model):
    """search report model"""

    query = models.CharField(max_length=1000)
    uid = models.IntegerField(null=False, default=0)
    start_domain = models.CharField(max_length=500)
    destination_domain = models.CharField(max_length=500)
    start_page = models.CharField(
        max_length=500, null=True, default=None, blank=True
    )
    destination = models.CharField(max_length=500, blank=True)
    destination_type = models.CharField(max_length=100)
    search_date = models.DateTimeField(null=False, default=timezone.now())
    srp_ranking = models.IntegerField()
    srp_status = models.IntegerField(default=0)
    device = models.CharField(max_length=50, null=True)
    add_question_status = models.IntegerField(null=True)
    ip = models.CharField(max_length=50)

    class Meta:
        verbose_name = "search report"
        verbose_name_plural = "search reports"
        db_table = "search_report"

    def __str__(self):
        return self.query
