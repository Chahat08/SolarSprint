from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'solarsprint'

urlpatterns = [
    path('', views.index, name='index'),
    path('/home', views.index, name='home'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
    url(r'^account_details/$', views.account_details, name='account_details'),
]









