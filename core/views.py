from django.shortcuts import render, get_object_or_404
from .models import Product, Category

def home(request):
    # Get all available products
    products = Product.objects.filter(is_available=True)
    return render(request, 'index.html', {'products': products})

def product_detail(request, slug):
    # Get one specific product or return a 404 error if it doesn't exist
    product = get_object_or_404(Product, slug=slug, is_available=True)
    return render(request, 'detail.html', {'product': product})