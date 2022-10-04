from rest_framework import serializers
from .models import Product_bot

class Product_bot_serializer(serializers.ModelSerializer):
    class Meta:
        model = Product_bot
        fields = '__all__'