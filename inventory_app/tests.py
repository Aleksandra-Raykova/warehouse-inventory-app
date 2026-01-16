from django.test import TestCase
from inventory_app.models import Category, Item


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

    def test_item_has_negative_total_stock_should_return_invalid_total_stock(self):
        i = Item.objects.create(name='asd', total_stock=6, item_category=self.c)
        i.total_stock -= 7
        self.assertEqual(i.stock_status, "Invalid total stock")
