from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('api/login/', LoginAPI.as_view(), name='login-api'),
]
