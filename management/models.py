from django.db import models
from django.core.validators import MaxValueValidator 

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


class Products(models.Model):
    title = models.CharField(max_length=30,null=True,blank=True)
    price = models.IntegerField(null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    category = models.CharField(null=True,blank=True,max_length=30,choices=Given_categories,default=1)
    stars = models.IntegerField(null=True,blank=True,validators=[MaxValueValidator])
    Image = models.FileField(null=True,blank=True)
    Image1 = models.FileField(null=True,blank=True)
    Image2 = models.FileField(null=True,blank=True)
    availability = models.BooleanField(null=True,blank=True,default=True)
    latestArrival = models.BooleanField(null=True,blank=True,default=False)
    bestSeller = models.BooleanField(null=True,blank=True,default=False)

    def __str__(self):
        return self.title + '---' + str(self.category)
    
