from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='rsp1'),
    path('/list', views.rsp_list, name='rsp1/list'),
]