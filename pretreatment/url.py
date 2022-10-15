from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='pre'),
    path('/list', views.pretreatment_list, name="pre/list"),
]