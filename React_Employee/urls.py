from django.urls import path
from .views import *

urlpatterns = [
    path('', EmployeeView.as_view(), name='employee-react')
]