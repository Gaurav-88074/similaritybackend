
from django.contrib import admin
from django.urls import path,include
from api import urls
urlpatterns = [
    path('', include(urls)),
]
