from django.urls import path
from .views import index, detail

urlpatterns = [
    path('', index),
    path('detail/<pk>', detail)
]