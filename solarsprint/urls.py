from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'solarsprint'

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]









