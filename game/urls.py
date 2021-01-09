"""game URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from solarsprint import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^$',views.index,name='index'),
    url(r'home/', views.index, name='home'),
    url(r'^log-in/', views.log_in, name='log_in'),
    url(r'^account/', views.account_details, name='account_details'),
    url(r'^special/',views.special,name='special'),
    url(r'^solarsprint/',include('solarsprint.urls')),
    url(r'^logout/$', views.user_logout, name='logout'),
]
