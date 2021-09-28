from django.db import models


# Create your models here.
class User(models.Model):
    userId = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


class Item(models.Model):
    itemId = models.IntegerField()
    name = models.CharField(max_length=100)
    imageURL = models.CharField(max_length=100)
    websiteURL = models.CharField(max_length=100)


class Wishlist(models.Model):
    wishListId = models.IntegerField()
    userid = models.IntegerField()
    password = models.IntegerField()
