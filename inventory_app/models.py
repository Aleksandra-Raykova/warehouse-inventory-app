from django.db import models


class Category(models.Model):
    """
    Category of each item. Many (items) to one (category) relation
    Category has only 'name' max to 50 chars
    """

    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Category: {self.name}"


class Item(models.Model):
    """
    All items in the warehouse
    Items have name, total_stock availability, and item_category (relation to Category model)
    Items have property stock_status - Out (if stock = 0), Low (if 0 < stock <= 5) and OK (if stock > 5)
    """
    name = models.CharField(max_length=50)
    total_stock = models.PositiveIntegerField()
    item_category = models.ForeignKey(to=Category, on_delete=models.PROTECT)

    @property
    def stock_status(self):
        if self.total_stock == 0:
            return "Out"
        elif 0 < self.total_stock <= 5:
            return "Low"
        elif self.total_stock > 5:
            return "OK"

    def __str__(self):
        return f"Item: {self.name}, {self.total_stock}, {self.item_category}"
