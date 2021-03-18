from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Product(models.Model):
    name = models.CharField(max_length=100)
    photo = models.CharField(max_length=100)
    rating = models.IntegerField()
    editorial_review = models.TextField(max_length=250)

    def __str__(self):
        return self.name

class Review(models.Model):
    review = models.TextField(max_length=250)

    def __str__(self):
        return self.review

# M:M relationship
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)



# class Profile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     image = models.ImageField(default='default.jpg', upload_to='profile_pics')
#     join_date = models.DateTimeField(default=timezone.now)
#     # join_Date = models.DateField()is_Del=models
#     #add 1: M assoc
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
