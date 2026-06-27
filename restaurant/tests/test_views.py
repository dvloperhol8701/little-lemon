from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from restaurant.models import Menu  # Changed from MenuItem to Menu
from restaurant.serializers import MenuSerializer  # Changed from MenuItemSerializer to MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        # Add a few test instances of the Menu model to the temporary test database
        Menu.objects.create(title="Pizza", price=12.00, inventory=50)
        Menu.objects.create(title="Burger", price=8.50, inventory=30)

    def test_getall(self):
        # 1. Retrieve all items from the test database
        menu_items = Menu.objects.all()
        
        # 2. Serialize the database data
        serializer = MenuSerializer(menu_items, many=True)
        
        # 3. Fetch the response from your actual endpoint view
        response = self.client.get('/restaurant/menu/') 
        
        # 4. Run assertions to check if the status is 200 OK and data matches perfectly
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)