from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"Category: {self.name}"


class Item(models.Model):
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
        else:
            return "Invalid total stock"

    def __str__(self):
        return f"Item: {self.name}, {self.total_stock}, {self.item_category}"
