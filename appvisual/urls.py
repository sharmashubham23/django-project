from django.contrib import admin
from django.urls import path
from appvisual import views
urlpatterns = [
    path("", views.index, name="Home"),
    path("data/", views.data, name="data"),
]
