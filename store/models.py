from django.db import models
from django.db.models.fields import DecimalField
from django.db.models.fields.related import ForeignKey

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    created_date = models.DateField(auto_now_add=True)
    update_date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
