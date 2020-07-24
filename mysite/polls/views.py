'''
@Author: Yang
@Date: 2019-10-28 09:58:23
@LastEditors: Yang
@LastEditTime: 2019-10-28 09:59:52
@FilePath: /mysite/polls/views.py
@Description: 
'''
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
