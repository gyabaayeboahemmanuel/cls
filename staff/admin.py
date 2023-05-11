from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header = "Customary Lands Secretariat Admin Dashboard"
admin.site.site_title = "Customary Lands Secretariat"
admin.site.index_title = "Welcome to Customary Lands Secretariat Admin"
admin.site.register(Profile)