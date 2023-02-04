from django.test import TestCase
from restaurant.views import MenuItemsView
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class TestMenuView(TestCase):
    def setUp(self):
        Menu.objects.create(Title="Curry", Price=50, Inventory=1)
        Menu.objects.create(Title="Salad", Price=50, Inventory=1)
        Menu.objects.create(Title="Ice Tea", Price=50, Inventory=1)

    def test_getall(self):
        item1 = Menu.objects.get(Title="Curry")
        item1_serialized = MenuSerializer(item1)
        self.assertEqual(item1_serialized.data['Title'], "Curry")