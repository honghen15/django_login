from django.conf.urls import include, url
from .views import *
from django.views.generic import TemplateView
from django.urls import path

urlpatterns = [

    path('', index, name='index'),
    path('callback', callback, name='callback'),
    path('home/', home, name='home'),

    path('login/', user_login, name="user_login"),
    path('success/', success, name='user_success'),
    path('logout/', user_logout, name="user_logout"),

    path('photos/', search, name='photos'),
    path('test/', watchphotos, name='watchphotos'),
    path('photo/<str:clientid>/', photodetail, name='photodetail'),
]
