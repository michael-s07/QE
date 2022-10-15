from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='rsp45'),
    path('/list', views.rsp45_list, name="rsp45/list"),
]