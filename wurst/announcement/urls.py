from django.urls import path, include

from . import views

urlpatterns = [
    path('service', views.announcement),
]
