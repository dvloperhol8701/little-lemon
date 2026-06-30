from django.test import TestCase
from django.contrib.auth.models import User      # <-- Import the User model
from rest_framework.test import APIClient
from rest_framework import status
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        
        # 1. Create a temporary test user in the test database
        self.user = User.objects.create_user(username='testuser', password='password123')
        
        # 2. Force authenticate your test client session
        self.client.force_authenticate(user=self.user)
        
        # 3. Seed your test data item
        Menu.objects.create(title="Ice Cream", price=80, inventory=50)

    def test_getall(self):
        # Now the client has permission clear clearance to execute the read request
        response = self.client.get('/restaurant/menu/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)