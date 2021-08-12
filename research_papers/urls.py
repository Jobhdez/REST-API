from django.contrib import admin
from django.urls import path, include
import api

urlpatterns = [
    path('research-papers/', include('api.urls')),
]
