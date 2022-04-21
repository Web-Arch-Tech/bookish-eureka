from django.urls import path 
from . import views # . (pointer means the current file)

urlpatterns = [
    path('', views.taskList, name='tasks'),
]
