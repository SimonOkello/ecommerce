from django.shortcuts import render


def index(request):
    return render(request, 'eshop/index.html', {})

def shop(request):
    return render(request, 'eshop/shop.html', {})

def productinfo(request):
    return render(request, 'eshop/shop-details.html', {})

def cart(request):
    return render(request, 'eshop/shopping-cart.html', {})

def checkout(request):
    return render(request, 'eshop/checkout.html', {})