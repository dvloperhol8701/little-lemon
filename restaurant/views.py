from django.shortcuts import render
from .models import Menu  # Import the Menu model

def index(request):
    # Fetch all items from your restaurant_menu table
    menu_data = Menu.objects.all()

    # Pass that data to your index.html template inside a dictionary
    context = {'menu': menu_data}
    return render(request, 'index.html', context)