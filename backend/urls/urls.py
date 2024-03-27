"""main url module"""
from django.conf import settings
from django.urls import include, path

from backend.apps.dashboard import controller as dashboard_api_views

urlpatterns = [
    path(
        "health",
        dashboard_api_views.ServiceCheckAPI.as_view(),
        name="search.service_check_api",
    ),
    path(
        "api/<int:version>/weather-history",
        dashboard_api_views.WeatherHistoryApi.as_view(),
        name="search.entities-search-api",
    )
]

if getattr(settings, "IS_DEBUG_TOOL_ACTIVE", False):
    urlpatterns.extend(
        [
            path("__debug__/", include("debug_toolbar.urls")),
        ]
    )
