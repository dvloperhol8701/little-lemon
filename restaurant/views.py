from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, viewsets, permissions
from .models import Menu, Booking
from .serializers import MenuSerializer, UserSerializer, BookingSerializer

# 1. Standard HTML Template View for Homepage
def index(request):
    menu_data = Menu.objects.all()
    context = {'menu': menu_data}
    return render(request, 'index.html', context)


# 2. REST API View for Menu Items (Handles GET & POST)
class MenuItemsView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# 3. REST API View for a Single Menu Item (Handles GET, PUT, DELETE)
class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


# 4. REST API View for Users
class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# 5. BookingViewSet for automated Table Booking CRUD operations (Locked by Djoser/DRF Auth)
class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]