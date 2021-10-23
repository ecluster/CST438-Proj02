from django.db import models


# Create your models here.
class User(models.Model):
    userId = models.IntegerField()
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username


class Item(models.Model):
    itemId = models.IntegerField()
    name = models.CharField(max_length=100)
    imageURL = models.CharField(max_length=2000)
    websiteURL = models.CharField(max_length=2000)

    def __str__(self):
        return self.name


class Wishlist(models.Model):
    wishListId = models.IntegerField()
    userid = models.IntegerField()
    itemId = models.IntegerField()

    def __int__(self):
        return self.wishListId
