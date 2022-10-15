from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='alizarine'),
    path('/list', views.alizarine_list, name='alizarine/list'),
]