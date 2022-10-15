from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='rsp23'),
    path('/list', views.rsp23_list, name='rsp23/list'),
]