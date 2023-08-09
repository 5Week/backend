from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'accountapp'

urlpatterns = [
    path('signup', views.signup_view, name='signup'),
    path('', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
]
