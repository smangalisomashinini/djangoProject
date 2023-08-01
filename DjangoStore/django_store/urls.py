from django.urls import path
from . import views

urlpatterns = [path('', views.index, name='index'),
               path('userReg/', views.userReg, name='userReg'),
               path('insertuser/', views.insertuser, name='insertuser')
               ]