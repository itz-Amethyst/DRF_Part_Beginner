from django.urls import path
from .views import PostListView, PostDetailView
urlpatterns = [
    path('', PostListView.as_view()),
    path('post_detail/<int:post_id>', PostDetailView.as_view())
]