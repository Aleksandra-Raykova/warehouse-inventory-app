from django.test import TestCase
from inventory_app.models import Category, Item
from rest_framework.test import APITestCase
from django.urls import reverse
from rest_framework import status

""" Run tests with 'python manage.py test inventory_app' command """

class ItemStockStatusTest(TestCase):
    def setUp(self):
        self.c = Category.objects.create(name='asd')

    def test_item_has_zero_total_stock_should_return_out(self):
        i = Item.objects.create(name='asd', total_stock=0, item_category=self.c)
        self.assertEqual(i.stock_status, "Out")

    def test_item_has_1_total_stock_should_return_low(self):
        i = Item.objects.create(name='asd', total_stock=1, item_category=self.c)
        self.assertEqual(i.stock_status, "Low")

    def test_item_has_5_total_stock_should_return_low(self):
        i = Item.objects.create(name='asd', total_stock=5, item_category=self.c)
        self.assertEqual(i.stock_status, "Low")

    def test_item_has_6_total_stock_should_return_ok(self):
        i = Item.objects.create(name='asd', total_stock=6, item_category=self.c)
        self.assertEqual(i.stock_status, "OK")


class ItemsListViewTest(APITestCase):
    def test_get_items(self):
        category = Category.objects.create(name="Test Category")
        Item.objects.create(name="Item 1", total_stock=10, item_category=category)
        Item.objects.create(name="Item 2", total_stock=0, item_category=category)

        url = reverse("items")
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_post_item(self):
        category = Category.objects.create(name="Test Category")
        url = reverse("items")
        data = {"name": "New Item", "total_stock": 10, "item_category": category.id}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Item.objects.count(), 1)

    def test_post_invalid_item(self):
        url = reverse("items")
        data = {}

        response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class ItemViewTest(APITestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.category2 = Category.objects.create(name="Test Category 2")
        self.item1 = Item.objects.create(name="Item 1", total_stock=10, item_category=self.category)
        self.item2 = Item.objects.create(name="Item 2", total_stock=0, item_category=self.category)
        self.url = reverse(viewname="show_one_item", kwargs={"pk": self.item1.id})

    def test_get_item_by_id_correct(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["name"], "Item 1")
        self.assertEqual(response.data["id"], 1)
        self.assertEqual(response.data["total_stock"], 10)

    def test_put_item_correct(self):
        # changed name, total_stock and item_category
        data = {"name": "New Item Name", "total_stock": 5, "item_category": self.category2.id}

        response = self.client.put(path=self.url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        item = Item.objects.get(id=1)
        self.assertEqual(item.name, "New Item Name")
        self.assertEqual(item.total_stock, 5)
        self.assertEqual(item.item_category, self.category2)

    def test_put_item_no_data_should_return_http_400(self):
        data = {}

        response = self.client.put(path=self.url, data=data, format="json")

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn("name", response.data)
        self.assertIn("total_stock", response.data)
        self.assertIn("item_category", response.data)

    def test_delete_item(self):
        response = self.client.delete(path=self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertNotIn(self.item1, Item.objects.all())
        self.assertIn(self.item2, Item.objects.all())

