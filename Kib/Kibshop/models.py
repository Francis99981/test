from django.db import models


class Shopping(models.Model):
    name= models.CharField(max_length=200, null=True)
    shopping = models.TextField()

    def __str__(self):
        return self.shopping
 

class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class OrderModel(models.Model):
    created_on = models.DateTimeField(auto_now_add=True)
    items = models.ManyToManyField('Shopping', 'order',blank=True)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200, null=True)
    phone_number = models.IntegerField(max_length=12, null=True)
    location = models.CharField(max_length=200, null=True)
    is_paid = models.BooleanField(default=False)
    is_shipped = models. BooleanField(default=False)

    def __str__(self):
        return f'Order: {self.created_on.strftime("%b %d %I %M %P")}'

