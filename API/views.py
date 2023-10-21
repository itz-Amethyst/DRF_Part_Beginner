from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from API.models import Post
from serializer import PostSerializer


# Create your views here.


@api_view(['GET'])
def index(request):
    try:
        p = Post.objects.get(pk = 100)

    except:
        return Response({'message': "not Found"} , status = status.HTTP_404_NOT_FOUND)
