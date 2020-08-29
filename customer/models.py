from django.db import models
from management.models import *
from django.contrib.auth.models import User

# Create your models here.
Given_categories = (
    ("Mens-Shirt","Mens-Shirt"),
    ("Mens-Tshirt","Mens-Tshirt"),
    ("Mens-Jeans","Mens-Jeans"),
    ("Mens-Kurta","Mens-Kurta"),
    ("Mens-Blazer","Mens-Blazer"),
    ("Womens-Top","Womens-Top"),
    ("Womens-Dresses","Womens-Dresses"),
    ("Womens-Jeans","Womens-Jeans"),
    ("Womens-Saree","Womens-Saree"),
    ("Womens-Western wear","Womens-Western wear"),
    ("Kids-Boys","Kids-Boys"),
    ("Kids-Girls","Kids-Girls"),
    ("Kids-Infants","Kids-Infants"),
)

class Add_To_Cart(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    cloth = models.ForeignKey(Products,on_delete=models.CASCADE,null=True,blank=True)
    quantity = models.IntegerField(null=True,blank=True,default=1)
    confirmation = models.BooleanField(null=True,blank=True,default=False)

    def __str__(self):
        return self.cloth.title
    
class ContactUs(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    name = models.CharField(max_length=200,null=True,blank=True)
    email = models.CharField(max_length=50,null=True,blank=True)            
    subject = models.CharField(max_length=100,null=True,blank=True)
    message = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name

