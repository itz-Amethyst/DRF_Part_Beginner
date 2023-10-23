from  django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name='index_page'),
    path('todo-json/', todo_json, name='todo_json_page')
]