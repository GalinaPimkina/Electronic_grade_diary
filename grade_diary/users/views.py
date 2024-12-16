from django.http import HttpResponse
from django.shortcuts import render

def func(request):
    return HttpResponse('hello from app users')
