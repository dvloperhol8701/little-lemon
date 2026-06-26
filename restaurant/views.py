from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, viewsets  # <-- Added viewsets here
from .models import Menu, Booking              # <-- Added Booking model
from .serializers import MenuSerializer, UserSerializer, BookingSerializer  # <-- Added BookingSerializer

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


# NEW - Step 3: BookingViewSet for automated Table Booking CRUD operations
from rest_framework import viewsets, permissions # <-- Make sure permissions is imported

# ... (rest of your views stay the same)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated] # <-- Adds the login lock!