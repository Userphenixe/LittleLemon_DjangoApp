from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.test import TestCase
from restaurant.models import Menu
import json

class MenuViewTest(TestCase):

    def setUp(self):
        # Create a test user and generate token for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client = APIClient()

        # Use token authentication for future requests
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

        # Create test Menu items
        Menu.objects.create(Title="Pizza", Price=10.99, Inventory=50)
        Menu.objects.create(Title="Burger", Price=8.99, Inventory=30)
        Menu.objects.create(Title="Pasta", Price=12.50, Inventory=20)

    def test_getall(self):
        # Perform a GET request using the authenticated client
        response = self.client.get(reverse('MenuItemsView'))

        # Expected serialized data
        expected_data = [
            {'id': Menu.objects.get(Title="Pizza").id, 'Title': 'Pizza', 'Price': '10.99', 'Inventory': 50},
            {'id': Menu.objects.get(Title="Burger").id, 'Title': 'Burger', 'Price': '8.99', 'Inventory': 30},
            {'id': Menu.objects.get(Title="Pasta").id, 'Title': 'Pasta', 'Price': '12.50', 'Inventory': 20},
        ]

        # Ensure response status is 200 OK
        self.assertEqual(response.status_code, 200)

        # Parse the response JSON
        response_data = json.loads(response.content)

        # Check if the response data matches the expected data
        self.assertEqual(response_data, expected_data)
