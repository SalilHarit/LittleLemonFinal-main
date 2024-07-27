from django.test import TestCase, Client
from django.urls import reverse
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer
import json

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu1 = Menu.objects.create(Title="Tomato Pizza", Price=10.99, Inventory=50)
        self.menu2 = Menu.objects.create(Title="Pepperoni Pizza", Price=12.99, Inventory=30)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        expected_json = json.dumps(serializer.data)
        self.assertEqual(expected_json, response.content.decode())
