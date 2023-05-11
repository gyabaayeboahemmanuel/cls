from django.urls import path
app_name = "allocation"
from .views import *

urlpatterns = [
    path ("allocate/", allocate, name="allocate"),
]
