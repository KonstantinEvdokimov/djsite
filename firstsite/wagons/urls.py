from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('wagons/', index, name='home'), # http://127.0.0.1:8000/
    path('types/<int:typeid>/', categories, name='types'),# http://127.0.0.1:8000/types/
    re_path(r'^archive/(?P<year>[0-9]{4})/', archive, name='archive'), # http://127.0.0.1:8000/archive/2020/
]

