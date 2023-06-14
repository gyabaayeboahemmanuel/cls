"""cls URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from staff.views import *
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = ( [
    path('admin/', admin.site.urls),
    path('client/', include('client.urls')),
    path('allocation/', include('allocation.urls')),
    path('lands/', include('lands.urls')),
    # path('staff/', include('staff.urls')),
    path('chief/', include('chief.urls')),
    path('', loginIndex),
    # path('accounts/login', loginIndex),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('dashboard', admindashboard, name="admin_dashboard"),
    path('dashboard/chief_records', admin_chief_records, name="admin_chief_records"),
    path('dashboard/chief_records/add_chief', admin_add_chief, name="admin_add_chief"),
    path('dashboard/chief_records/edit_chief/<int:id>', admin_edit_chief, name="admin_edit_chief"),
    path('dashboard/chief_records/view_chief/<int:id>', admin_view_chief, name="admin_view_chief"),
    path('dashboard/chief_records/delete_chief/<int:id>', admin_delete_chief, name="admin_delete_chief"),
    path('dashboard/staff_records/add_staff', admin_add_staff, name="admin_add_staff"),
    path('dashboard/staff_records', admin_staff_records, name="admin_staff_records"),
    path('dashboard/staff_records/<str:username>/profile', admin_staff_profile, name="admin_staff_profile"),
    path('dashboard/staff_records/<str:username>/activate', admin_staff_activate, name="admin_staff_activate"),
    path('dashboard/staff_records/<str:username>/deactivate', admin_staff_deactivate, name="admin_staff_deactivate"),
    path('dashboard/land_records/add_land', admin_add_land, name="admin_add_land"),
    path('dashboard/land_records/edit_land/<int:id>', admin_edit_land, name="admin_edit_land"),
    path('dashboard/land_records', admin_land_records, name="admin_land_records"),
    path('dashboard/client_records', admin_client_records, name="admin_client_records"),
    path('dashboard/client_records/add_client', admin_add_client, name="admin_add_client"),
    path('dashboard/allocation_records', admin_allocation_records, name="admin_allocation_records"),
    path('dashboard/allocation_records/make_allocation', admin_make_allocation, name="admin_make_allocation"),
    path('dashboard/chief_records/edit_allocation/<int:id>', admin_edit_allocation, name="admin_edit_allocation"),
    path('dashboard/chief_records/view_allocation/<int:id>', admin_view_allocation, name="admin_view_allocation"),
    path('dashboard/chief_records/delete_allocation/<int:id>', admin_delete_allocation, name="admin_delete_allocation"),
    path("accounts/", include("django.contrib.auth.urls")),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
 + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
