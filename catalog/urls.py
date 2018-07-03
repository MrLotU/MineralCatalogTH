from django.urls import path
from .views import index, detail, random_mineral, search, filter_by_letter, group

app_name = 'catalog'
urlpatterns = [
    path('', index, name='home'),
    path('detail/<pk>', detail, name='detail'),
    path('random', random_mineral, name='random'),
    path('search', search, name='search'),
    path('filter', filter_by_letter, name='filter'),
    path('group', group, name='group')
]