from django.urls import path
from .views import index, detail, random_mineral

app_name = 'catalog'
urlpatterns = [
    path('', index, name='home'),
    path('detail/<pk>', detail, name='detail'),
    path('random', random_mineral, name='random')
]