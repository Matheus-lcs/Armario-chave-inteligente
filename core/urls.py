from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("api/status/", views.status_api, name="status_api"),
    path(
        "api/status_nicho/",
        views.status_nicho_view,
        name="status_nicho",
    ),
    path(
        "api/status_nichos/",
        views.api_status_nicho,
        name="api_status_nicho",
    ),
]
