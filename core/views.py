from itertools import product
from django.shortcuts import render

from store.models import Product

def frontPage(request):
    products = Product.objects.filter(status=Product.ACTIVE)[0:20]
    context = {
        'products' : products
    }
    return render(request,'core/frontpage.html',context)

def about(request):
    return render(request,'core/about.html')
