from django.test import TestCase
from restaurant.models import Menu

class MenuTest(TestCase):

    def test_get_item(self):
        item = Menu.objects.create(Title="Beef", Price=80, Inventory=100)
        self.assertEqual(item, "Beef : 50")
