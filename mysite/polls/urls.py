'''
@Author: Yang
@Date: 2019-10-28 10:00:36
@LastEditors: Yang
@LastEditTime: 2019-10-28 10:00:53
@FilePath: /mysite/polls/urls.py
@Description: 
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
