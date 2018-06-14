from django.urls import path
from .views import index, detail, random_mineral

urlpatterns = [
    path('', index),
    path('detail/<pk>', detail),
    path('random', random_mineral)
]