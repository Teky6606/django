from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# tạo CSDL bảng Customers
class Customers(models.Model):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=False)
    name = models.CharField(max_length=200, null= True)
    email = models.EmailField(max_length=200)

    def __str__(self):
        return self.name

# tạo bảng CSDL cho sản phẩm
class products(models.Model):
    name_products =models.CharField(max_length=120)
    price_products = models.FloatField()
    image = models.ImageField(blank=False, null=True)
    def __str__(self):
        return self.name
    
    @property
    def getUrlImage(self):
        try:
            url = self.image.url
        except:
            url =''
        return url


class oders(models.Model):
    customers = models.ForeignKey(Customers, on_delete=models.SET_NULL, blank=False , null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    complete = models.BooleanField(default= False, null=True ,blank=False)

    def __str__(self):
        return str(self.id)
    
class orderItems(models.Model):
   customers = models.ForeignKey(Customers, on_delete=models.SET_NULL, blank=False , null=True)
   order = models.ForeignKey(oders ,on_delete=models.SET_NULL, blank=False , null=True)
   date_buy = models.DateTimeField(auto_now_add=True)


