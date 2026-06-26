from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    
    # Menu API Endpoints - Step 5
    path('menu/', views.MenuItemsView.as_view(), name='menu-items'),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view(), name='single-menu-item'),
    
    # User API Endpoints
    path('users/', views.UserListView.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetailView.as_view(), name='user-detail'),
]