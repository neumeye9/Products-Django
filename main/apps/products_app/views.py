from django.shortcuts import render, redirect
from . models import Products

# Create your views here.

def index(request):
    Products.objects.create(product_name="Shampoo",product_description="Used for washing your hair prior to conditioner", weight=3, price=5.00, cost=7.90, category="Health and Beauty")
    
    Products.objects.create(product_name="Conditioner", product_description="Use after Shampoo", weight=2,price=6.00, cost= 8.50)

    Products.objects.create(product_name="hairbrush", product_description="Tool to untangle hair", weight=2, price=6.00, cost=9.99)

    products = Products.objects.all()

    for product in products:
        print product.id, product.product_name, product.cost


    return render(request, 'products_app/index.html')