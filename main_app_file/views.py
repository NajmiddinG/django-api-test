from django.shortcuts import render, redirect
from .models import Product_bot
from django.http.response import HttpResponse, JsonResponse
from rest_framework import viewsets
from .serializers import Product_bot_serializer
from rest_framework import permissions
# Create your views here.

import openpyxl
from pathlib import Path

def testqilish(request):
    Product_bot.objects.all().delete()
    xlsx_file = Path('BotBaza 2.xlsx')
    wb_obj = openpyxl.load_workbook(xlsx_file)

    # Read the active sheet:
    sheet = wb_obj.active
    for row in sheet.iter_rows(max_row=3042, min_row=2):
        data = Product_bot.objects.create(
        product_id = row[0].value if row[0].value else "",
        name = row[1].value if row[1].value else "",
        description = row[2].value if row[2].value else "",
        price = row[3].value if row[3].value else 0,
        tags = row[4].value if row[4].value else "",
        imageUrl = row[5].value if row[5].value else "",
        optionName = row[6].value if row[6].value else "",
        hidden = row[7].value if row[7].value else "")
        data.save()
    return HttpResponse("Test muvafaqqiyatli yakunlandi!")


class Product_bot_view_set(viewsets.ModelViewSet):
    queryset = Product_bot.objects.all()
    serializer_class = Product_bot_serializer
    permission_classes = [permissions.AllowAny]