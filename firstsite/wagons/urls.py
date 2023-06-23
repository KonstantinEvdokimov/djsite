from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index), # http://127.0.0.1:8000/
    path('types/', categories),# http://127.0.0.1:8000/types/
]
