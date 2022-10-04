from django.contrib import admin
from .models import Product_bot

# Register your models here.

@admin.register(Product_bot)
class Product_bot_admin(admin.ModelAdmin):
    list_display = ('product_id', 'name', 'description', 'price', 'tags', 'imageUrl', 'optionName', 'hidden', 'weight', 'prepaymentPercent', 'hideBuyBtn', 'bonusesPercent')
    