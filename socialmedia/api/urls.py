from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    PostListCreateView, PostRetrieveUpdateDeleteView, 
    CommentListCreateView, FollowView, FeedView
)

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDeleteView.as_view(), name='post-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('follow/', FollowView.as_view(), name='follow'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]



