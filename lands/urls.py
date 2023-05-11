from django.urls import path
from .views import *

urlpatterns = [
    path ("add_land/", add_land, name="add_land"),
]
