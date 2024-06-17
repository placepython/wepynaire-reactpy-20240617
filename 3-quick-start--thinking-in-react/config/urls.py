"""
URL configuration for example project.
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("pages.urls")),
    path("reactpy/", include("reactpy_django.http.urls")),
]
