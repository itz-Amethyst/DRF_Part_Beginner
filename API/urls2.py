import requests

from .views import *

from django.urls import path, include
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post-viewset', PostView, basename = 'post')

urlpatterns = [
    # path('/postdetail', PostDetailView.as_view(), name='test'),
    path('', PostListView.as_view(), name='post'),
    path('/postdetail/<int:pk>', PostDetailView.as_view(), name='test')
]

urlpatterns += router.urls