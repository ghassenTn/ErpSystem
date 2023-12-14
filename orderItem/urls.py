from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('api/login/', LoginAPI.as_view(), name='login-api'),
    path('chat/', chat, name='chat'),
    path('api/users/', get_users, name='get_users'),
    path('api/groups/', get_groups, name='get_groups'),
    #path('register/', client_register,name='register')
]
