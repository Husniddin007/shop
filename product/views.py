from unicodedata import category

from django.shortcuts import render
from product.models import Product

def  product_list(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request,'product_list.html',context=context)

def  product_detail(request,product_id):
    products = Product.objects.get(id=product_id)
    related_products = Product.objects.filter(category=products.category).exclude(id=product_id)
    context = {
        'products':products,
        'related_products':related_products,
    }
    return render(request,'product_detail.html',context=context)
def about(request):
    return render(request,'about.html')

