from django.shortcuts import render
from rest_framework import generics , permissions
from rest_framework.pagination import PageNumberPagination

from React_Employee.models import Employee
from React_Employee.serializer import EmployeeSerializer


# Create your views here.

class EmployeeView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    # authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.AllowAny]
    # only work for this api with some customs
    pagination_class = PageNumberPagination

