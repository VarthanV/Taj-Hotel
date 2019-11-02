from django.db import models

# Create your models here.
from django.db import models

# Customer Details Model


class CustomerDetails(models.Model):
    u_id = models.CharField(max_length=50)
    name = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    address = models.TextField()


class SubItems(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity=models.CharField(max_length=200)


class Items(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    subitems = models.ManyToManyField(SubItems)


class Order(models.Model):
    items = models.ManyToManyField(Items)
    customer = models.ForeignKey(CustomerDetails, on_delete=models.DO_NOTHING)
    cost = models.IntegerField()
