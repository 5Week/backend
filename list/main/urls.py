from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'mainapp'

urlpatterns = [
    path('', views.main_view, name='main'),
    path('list', views.list_view, name='list'),
    path('mypage', views.mypage_view, name='mypage'),
    path('logout', views.logout_view, name='logout'),
    path('detail/<int:board_id>/', views.detail_view, name='detail')

]