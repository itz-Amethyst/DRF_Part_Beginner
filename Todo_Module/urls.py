from  django.urls import path
from .views import *

urlpatterns = [
    path('', Index, name='index_page'),
    path('todo-json/', todo_json, name='todo_json_page'),
    path('todo-w-serializer/', all_todos_w_serializer, name='all_todos_w_serializer'),
    path('todo-detail/<int:todo_id>', todo_detail_view, name='todo_detail_page'),
]