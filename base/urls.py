from django.urls import path
from base.views import index_view, process_url

app_name = 'base'

urlpatterns = [
    path('', index_view, name="index_view"),
    path('process_url/', process_url, name="process_url")
]