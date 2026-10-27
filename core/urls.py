from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('api/status/', views.status_api, name='status_api'),
    path('api/status_nichos/', views.api_status_nichos, name='status_nichos'),
]
