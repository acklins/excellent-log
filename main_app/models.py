from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from pyuploadcare.dj.models import ImageField

class Product(models.Model):
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=100) #ImageField(blank=True, manual_crop="")
    rating = models.IntegerField()
    editorial_review = models.TextField(max_length=250)

    def __str__(self):
        return self.name

class Profile(models.Model):
     user = models.OneToOneField(User, on_delete=models.CASCADE)
     profile_pic = ImageField(blank=True, manual_crop="")

     def __str__(self):
         return self.name

class Review(models.Model):
    review = models.TextField(max_length=250)

    def __str__(self):
        return self.review

# M:M relationship
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
