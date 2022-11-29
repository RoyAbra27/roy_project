from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name= models.CharField(max_length=50, null=False, blank=False)
    user= models.OneToOneField(User, on_delete=models.CASCADE,null=False, blank=False)
    _id=models.AutoField(primary_key=True,editable=False)
    def __str__(self) :
        return self.name


class Product(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    user =models.ForeignKey(User,on_delete=models.CASCADE,null=False, blank=False)
    description = models.CharField(max_length=50,null=False, blank=False)
    photo=models.ImageField(null=True,blank=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,null=False, blank=False)
    price = models.DecimalField(max_digits=100,decimal_places=2, default=1)

    def __str__(self) :
        return self.description


class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone = models.IntegerField()
    address = models.CharField(max_length=50)
    gender=models.CharField(max_length=10)
    def __str__(self):
        return self.address



class Order(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    user =models.ForeignKey(User,on_delete=models.CASCADE,null=False, blank=False)
    total_price= models.IntegerField(default=1, null=True,blank=True)
    createdTime=models.DateTimeField(auto_now_add=True)
    def __str__(self) :
        return self.user
    
    # product_id = models.ForeignKey(Product, on_delete=models.CASCADE, null=False,blank=False)
    # amount= models.IntegerField(default=1, null=True,blank=True)
    # total = models.IntegerField(default=1, null=True,blank=True)


class  OrderDetail(models.Model):
    _id=models.AutoField(primary_key=True,editable=False)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE, null=False,blank=False)
    prod=models.ForeignKey(Product,on_delete=models.CASCADE,null=False, blank=False)
    amount=models.IntegerField(default=1, null=True,blank=True)
    total_price= models.IntegerField(default=1, null=True,blank=True)
    def __str__(self) :
        return self.order_id

# adivertieshbtt
#pass 