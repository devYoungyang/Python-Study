'''
@Author: Yang
@Date: 2019-10-30 17:27:56
@LastEditors: Yang
@LastEditTime: 2019-10-30 17:29:50
@FilePath: /oa/hrs/url.py
@Description: 
'''
from django.urls import path

from hrs import views

urlpatterns = [
    path('', views.index, name='index'),
]
