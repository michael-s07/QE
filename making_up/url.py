from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='making'),
    path('/list', views.making_list, name='making/list')
]