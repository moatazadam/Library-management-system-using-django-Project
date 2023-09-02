from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self) :
        return self.name


class Book(models.Model):
    choices = [ # we make it as pairs so that one is showen to user and the other one is saved in database 
        ('available' ,'available'),
        ('sold' , 'sold'),
        ('rental' , 'rental')
    ]
    title = models.CharField(max_length=250)
    author = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=6 , decimal_places=2 , blank=True , null=True)
    photo_book = models.ImageField(upload_to='photos' , blank=True , null=True)
    photo_author = models.ImageField(upload_to='photos' , blank=True , null=True)
    Number_of_pages = models.IntegerField(max_length=4 , blank=True , null=True)
    retal_price_per_day = models.DecimalField(max_digits=6 , decimal_places=2 , blank=True , null=True)
    retal_period = models.IntegerField(max_length=3 , blank=True , null=True)
    total_rental = models.DecimalField(max_digits=6 , decimal_places=2 , blank=True , null=True)
    available = models.BooleanField(default=True)
    status = models.CharField(max_length=50 , choices=choices , blank=True , null=True)
    Category = models.ForeignKey(Category , on_delete=models.PROTECT)

    def __str__(self):
        return self.title     



