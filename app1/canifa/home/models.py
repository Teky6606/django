from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# tạo CSDL bảng Customers
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name
# create table database product
class product(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.ImageField( blank=False, null=True)
    def __str__(self):
        return self.name
    @property
    def imageurl(self):
        try:
            url = self.image.url
        except:
            url =''
        return url
# create table database order
class order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=False, null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    compete = models.BooleanField(default=False, null=True,blank=False)
    transaction_id = models.CharField(max_length=200)
    def __str__(self):
        return str(self.id)


class orderItems(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=False, null=True)
    order = models.ForeignKey(order, on_delete=models.SET_NULL, blank=False, null=True)

    quanlity = models.IntegerField(default=0)
    data_buy = models.DateTimeField(auto_now_add=True)

class shipping(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=False, null=True)
    order = models.ForeignKey(order, on_delete=models.SET_NULL, blank=False, null=True)
    address = models.CharField(max_length=200, null= True) 
    city = models.CharField(max_length=200, null= True) 
    state = models.CharField(max_length=200, null= True) 
    mobile = models.CharField(max_length=200, null= True) 
    data_ship = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address