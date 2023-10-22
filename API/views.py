
from rest_framework import status , permissions
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import generics
from rest_framework import mixins

from API.models import Post
from utils.CustomMethods import get_object
from .serializer import PostSerializer


# Create your views here.


# @api_view(['GET'])
# def index(request):
#     try:
#         p = Post.objects.get(pk = 100)
#
#     except:
#         return Response({'message': "not Found"} , status = status.HTTP_404_NOT_FOUND)
#
#     serializer = PostSerializer(p)
#
#     return Response(serializer.data)
#

##? API view from scratch
# class PostListView(APIView):
#
#     def get(self, request):
#         posts = Post.objects.all()
#         # For more than 1 object we should set many to true
#         data = PostSerializer(posts , many = True).data
#         return Response(data)
#
#     def post(self, request):
#         serializer = PostSerializer(data = request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
#
#
# class PostDetailView(APIView):
#
#     def get(self, request, post_id):
#         post = get_object(self , post_id)
#
#         serializer = PostSerializer(post)
#
#         return Response(serializer.data)
#
#     def put(self, request, post_id):
#
#         post = get_object(self, post_id)
#
#         serializer = PostSerializer(post , data = request.data)
#         if serializer.is_valid():
#             return Response(serializer.data)
#         return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, post_id):
#         post = get_object(self, post_id)
#         post.delete()
#         return Response(status = status.HTTP_204_NO_CONTENT)


##* Viewsets found on document but it's custom all this methods is implemented no need to write again
# class PostList(viewsets.ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def list(self, request):
#         posts = Post.objects.all()
#         # For more than 1 object we should set many to true
#         data = PostSerializer(posts , many = True).data
#         return Response(data)
#
#     def create(self, request):
#         serializer = PostSerializer(data = request.data)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors , status = status.HTTP_400_BAD_REQUEST)



##! These methods used generic methods it's easier and implemented some functions before

# class PostListView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#
#     def get(self, request, **kwargs ):
#         return self.list()
#
#     def post(self, request, **kwargs ):
#         return self.create()


# class PostDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [permissions.AllowAny]
#
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)



##! This one is exactly like up but in shorter version not recommended if you want to play with data more customizable than
class PostListView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]


#? Note: diff between update and partial update is partial only send specific data f.e.g we have a model named user it has 3 prop username, email, password if you want to update only username use partial update
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]



## * Note all in one CRUD even with id but not customizable all static
class PostView(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]