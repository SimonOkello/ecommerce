from django.shortcuts import render
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView


# Create your views here.
class HomeView(ListView):
    model = Item
    template_name = 'home-page.html'

    
class ItemDetailView(DetailView):
    model = Item
    template_name = 'product-page.html'

def checkout(request):
    return render(request, 'checkout-page.html', {})