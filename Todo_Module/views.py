from django.shortcuts import render
from django.contrib.auth import get_user_model

from drf_spectacular.utils import extend_schema , OpenApiResponse

from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status , permissions
from rest_framework.views import APIView
from rest_framework import generics , mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from rest_framework.authentication import BasicAuthentication, TokenAuthentication

from Todo_Module.models import Todo
from Todo_Module.serializer import TodoSerializer , UserSerializer
from utils.CustomMethods import get_object


# Create your views here.

User = get_user_model()

#! Options
class TodosGenericApiViewOptions(PageNumberPagination):
    invalid_page_message = 'This is a invalid message'
    last_page_strings = ('last',)
    page_size = 2
    page_query_description = 'tests tsfsd fdsgds page query'
    page_size_query_description = 'Number of results to return per page.'


class TodosViewSetsAPiViewOptions(LimitOffsetPagination):
    # Same as page_size
    default_limit = 1



def Index( request ):
    context = {
        'todos': Todo.objects.order_by('-priority').all()
    }
    return render(request , 'Todo_Module/Index.html' , context)

#region plainApi

# class TodosListApiView(APIView):
#
#     permission_classes = [permissions.AllowAny]
#     def get( self, request: Request ):
#         todos = Todo.objects.order_by('-priority').all()
#         todo_serializer = TodoSerializer(todos , many = True)
#         return Response({'todos': todo_serializer.data} , status = status.HTTP_200_OK)
#
#     def post( self, request: Request ):
#         serializer = TodoSerializer(data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status = status.HTTP_201_CREATED)
#         return Response(serializer.errors , status.HTTP_400_BAD_REQUEST)
#
#
# class TodosDetailApiView(APIView):
#     permission_classes = [permissions.AllowAny]
#
#     @staticmethod
#     def get_todo( todo_id:int ):
#         todo = get_object(object_id = todo_id, object = Todo)
#         return todo
#
#     def get( self, request:Request, todo_id ):
#         todo = self.get_todo(todo_id)
#         serializer = TodoSerializer(todo)
#         return Response(serializer.data, status.HTTP_200_OK)
#
#     def put( self , request: Request , todo_id ):
#         todo = self.get_todo(todo_id)
#         serializer = TodoSerializer(todo, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status.HTTP_200_OK)
#         return Response(serializer.errors , status.HTTP_400_BAD_REQUEST)
#
#     def delete( self , request: Request , todo_id ):
#         todo = self.get_todo(todo_id)
#         todo.delete()
#         return Response(None, status.HTTP_204_NO_CONTENT)
#

#endregion


##region Mixin Parts


class TodosListMixinApiView(mixins.ListModelMixin , mixins.CreateModelMixin , generics.GenericAPIView):
    queryset = Todo.objects.order_by('-priority').all()
    serializer_class = TodoSerializer
    authentication_classes = [TokenAuthentication]
    # permission_classes = [permissions.AllowAny]

    @extend_schema(
        request = TodoSerializer ,
        responses = {201: TodoSerializer} ,
        description = 'this api is used for get all todos list'
    )
    def get( self , request: Request ):
        return self.list(request)

    @extend_schema(
        summary = 'Todo Registration' ,
        description = "This is POST method api, in which user data will be created and using the same user instance one Employee instance will be created" ,
        request = TodoSerializer ,
        responses = {
            200: OpenApiResponse(description = 'Json Response') ,
            400: OpenApiResponse(description = 'Validation error')
        }
    )
    def post( self , request: Request ):
        return self.create(request)


class TodosDetailMixinApiView(mixins.RetrieveModelMixin , mixins.UpdateModelMixin , mixins.DestroyModelMixin ,
                              generics.GenericAPIView):
    queryset = Todo.objects.order_by('-priority').all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny]

    # Note in Generic mixins should use pk as id

    def get( self , request: Request , pk ):
        return self.retrieve(request , pk)

    def put( self , request: Request , pk ):
        return self.update(request , pk)

    def delete( self , request: Request , pk ):
        return self.destroy(request , pk)

#endregion


# region Generics

class TodosGenericApiView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    # only work for this api with some customs
    pagination_class = TodosGenericApiViewOptions


class TodosDetailGenericApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny]
# endregion


#region ViewSets

class TodosViewSetApiView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    permission_classes = [permissions.AllowAny]
    # This without options
    # pagination_class = LimitOffsetPagination

    # with options
    pagination_class = TodosViewSetsAPiViewOptions

#endregion

class UserGenericApiView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


#region Users