from django.urls import path
app_name = "client"
from .views import *

urlpatterns = [
    path ("add/", add_client, name="add_client"),
]
