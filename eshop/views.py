from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView
from django.utils import timezone


# Create your views here.
class HomeView(ListView):
    model = Item
    paginate_by = 1
    template_name = 'home-page.html'


class ItemDetailView(DetailView):
    model = Item
    template_name = 'product-page.html'


def checkout(request):
    return render(request, 'checkout-page.html', {})

# Add To Cart View


def add_to_cart(request, slug):
    ordered_date = timezone.now()
    item = get_object_or_404(Item, slug=slug)
    order_item, created = OrderItem.objects.get_or_create(
        item=item, user=request.user, ordered=False)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    # Check if the order exists
    if order_qs.exists():
        order = order_qs[0]

    # Check if order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
            messages.info(request, "The item quantity was updated.")
            return redirect('products', slug=slug)
        else:
            
            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect('products', slug=slug)
    else:
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.item.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect('products', slug=slug)
    return redirect('products', slug=slug)

# Remove from Cart View


def remove_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    # Check if the order exists
    if order_qs.exists():
        order = order_qs[0]

    # Check if order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item, user=request.user, ordered=False)[0]
            order.items.remove(order_item)
            messages.info(request, "This item was removed to your cart.")
            return redirect('products', slug=slug)
        else:
            messages.info(request, "The item was was not in your cart.")
            return redirect('products', slug=slug)
    else:
        messages.info(request, "You do not have an active order.")
        return redirect('products', slug=slug)

    return redirect('products', slug=slug)
