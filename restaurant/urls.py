from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Menu API Endpoints - Step 5
    # Menu API Endpoints - Step 5
    path('menu/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='single-menu-item'),    
    # User API Endpoints
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
    
    # Token Authentication Endpoint - Step 4
    path('api-token-auth/', obtain_auth_token, name='api-token-auth'),
]