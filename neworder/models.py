from django.db import models
# Customer Details Model


class CustomerDetails(models.Model):
    u_id = models.TextField()
    name = models.TextField()
    phone_number = models.TextField()
    email = models.EmailField()
    address = models.TextField()


class SubItems(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    quantity = models.IntegerField()


class Items(models.Model):
    name = models.TextField()
    price = models.IntegerField()
    total_price=models.IntegerField()
    subitems = models.ManyToManyField(SubItems)


class OrderItem(models.Model):
    item = models.ForeignKey(Items, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField()
    total_price = models.IntegerField()


class Order(models.Model):
    invoice_no = models.TextField()
    ordered_items= models.ManyToManyField(OrderItem)
    customer = models.ForeignKey(CustomerDetails, on_delete=models.DO_NOTHING)
    advance = models.IntegerField()
    session=models.TextField()
    total = models.IntegerField()
    balance = models.IntegerField()
    date_placed = models.DateTimeField(auto_now_add=True)
    date_of_delivery = models.DateTimeField()
