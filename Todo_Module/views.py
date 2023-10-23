from django.http import HttpRequest , JsonResponse
from django.shortcuts import render

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status , permissions
from rest_framework.decorators import api_view , permission_classes

from Todo_Module.models import Todo


# Create your views here.


def Index(request):
    context = {
        'todos': Todo.objects.order_by('-priority').all()
    }
    return render(request, 'Todo_Module/Index.html', context)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def todo_json(request: Request):
    todos = list(Todo.objects.order_by('-priority').all().values('title', 'is_done'))

    return Response({'todos': todos}, status = status.HTTP_200_OK)