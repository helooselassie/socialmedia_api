from django.urls import path
from .views import CustomAuthToken
from .views import CustomTokenObtainPairView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import (
    PostListCreateView, PostRetrieveUpdateDeleteView, LoginView, 
    CommentListCreateView, FollowView, FeedView, RegisterUserView
)

urlpatterns = [
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDeleteView.as_view(), name='post-detail'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('follow/', FollowView.as_view(), name='follow'),
    path('feed/', FeedView.as_view(), name='feed'),
    path('api/users/login/', LoginView.as_view(), name='user_login'),
    path('users/login/', LoginView.as_view(), name='login'),
    path('users/login/', CustomAuthToken.as_view(), name='user-login'),
    path('users/register/', RegisterUserView.as_view(), name='user-register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]



