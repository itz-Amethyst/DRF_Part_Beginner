from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response

from API.models import Post
from .serializer import PostSerializer
from rest_framework import viewsets


# Create your views here.


@api_view(['GET'])
def index(request):
    try:
        p = Post.objects.get(pk = 100)

    except:
        return Response({'message': "not Found"}, status = status.HTTP_404_NOT_FOUND)

    serializer = PostSerializer(p)

    return Response(serializer.data)


class PostListView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        # For more than 1 object we should set many to true
        data = PostSerializer(posts, many = True).data
        return Response(data)

    def post(self, request):
        serializer = PostSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class PostList(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request):
        posts = Post.objects.all()
        # For more than 1 object we should set many to true
        data = PostSerializer(posts, many = True).data
        return Response(data)

    def create(self, request):
        serializer = PostSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)




class PostDetailView(APIView):

    def get(self, request, post_id):
        try:
            post = Post.objects.get(pk= post_id)
        except:
            return Response({'message': "not found"}, status = status.HTTP_404_NOT_FOUND)

        serializer = PostSerializer(post)

        return Response(serializer.data)
