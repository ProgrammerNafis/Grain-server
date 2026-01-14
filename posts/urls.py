from django.urls import path
from .views import PostList, PostDetail, CategoryList
from .views import RegisterUser, UserDashboard 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('posts/', PostList.as_view(), name='post-list'),
    path('posts/<slug:slug>/', PostDetail.as_view(), name='post-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # এখানে ইউজার লগইন করবে
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('dashboard/', UserDashboard.as_view(), name='dashboard'),
]
