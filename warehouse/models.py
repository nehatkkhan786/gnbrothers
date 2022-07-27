from unicodedata import category
from django.db import models





class Company(models.Model):
    name = models.CharField(max_length=200)

class Category(models.Model):
    name = models.CharField(max_length=200)


class Product(models.Model):
    name= models.CharField(max_length=200)
    price = models.IntegerField()
    weight = models.DecimalField(max_digits=4, decimal_places=2)
    image = models.ImageField(upload_to='uploads/')
    inStock = models.IntegerField(default=0)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

