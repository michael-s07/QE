from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='finish'),
    path('/list', views.finish_list, name='finish_list/list'),
]