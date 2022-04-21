from django.shortcuts import render
from django.http import HttpResponse
#function-based views.

def taskList(request):
    return HttpResponse('<h1>To Do list</h1>')