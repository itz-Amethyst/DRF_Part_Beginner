from django.http import HttpRequest , JsonResponse
from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status , permissions
from rest_framework.decorators import api_view , permission_classes
from rest_framework.views import APIView

from Todo_Module.models import Todo
from Todo_Module.serializer import TodoSerializer
from utils.CustomMethods import get_object


# Create your views here.


def Index(request):
    context = {
        'todos': Todo.objects.order_by('-priority').all()
    }
    return render(request, 'Todo_Module/Index.html', context)


class TodosListApiView(APIView):

    permission_classes = [permissions.AllowAny]
    def get( self, request: Request ):
        todos = Todo.objects.order_by('-priority').all()
        todo_serializer = TodoSerializer(todos , many = True)
        return Response({'todos': todo_serializer.data} , status = status.HTTP_200_OK)

    def post( self, request: Request ):
        serializer = TodoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status = status.HTTP_201_CREATED)
        return Response(serializer.errors , status.HTTP_400_BAD_REQUEST)


class TodosDetailApiView(APIView):
    permission_classes = [permissions.AllowAny]

    @staticmethod
    def get_todo( todo_id:int ):
        todo = get_object(object_id = todo_id, object = Todo)
        return todo

    def get( self, request:Request, todo_id ):
        todo = self.get_todo(todo_id)
        serializer = TodoSerializer(todo)
        return Response(serializer.data, status.HTTP_200_OK)

    def put( self , request: Request , todo_id ):
        todo = self.get_todo(todo_id)
        serializer = TodoSerializer(todo, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status.HTTP_200_OK)
        return Response(serializer.errors , status.HTTP_400_BAD_REQUEST)

    def delete( self , request: Request , todo_id ):
        todo = self.get_todo(todo_id)
        todo.delete()
        return Response(None, status.HTTP_204_NO_CONTENT)
