from django.urls import path
app_name = "chief"
from .views import *

urlpatterns = [
    path ("add_chief/", add_chief, name="add_chief"),
]
