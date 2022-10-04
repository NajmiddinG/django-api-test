from django.db import models

# Create your models here.

class Product_bot(models.Model):
    product_id = models.CharField(max_length=10, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(max_length=1000, blank=True, null=True)
    price = models.PositiveIntegerField(default=0)
    tags = models.CharField(max_length=255, blank=True, null=True)
    imageUrl = models.URLField(max_length=255, blank=True, null=True)
    optionName = models.CharField(max_length=255, blank=True, null=True)
    hidden = models.CharField(max_length=100, blank=True, null=True)
    weight = models.PositiveIntegerField(default=0)
    prepaymentPercent = models.IntegerField(default=0)
    hideBuyBtn = models.BooleanField(default=True, blank=True, null=True)
    bonusesPercent = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
