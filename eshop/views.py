from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404, redirect
from .models import Item, OrderItem, Order
from django.views.generic import ListView, DetailView, View
from . forms import CheckoutForm
from django.utils import timezone


# Create your views here.
class HomeView(ListView):
    model = Item
    paginate_by = 10
    template_name = 'index.html'


class OrderSummaryView(LoginRequiredMixin, View):
    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            return render(self.request, 'order_summary.html', {'object':order})

        except ObjectDoesNotExist:
            messages.error(self.request, 'You do not have an active order')
            return redirect('home')


class ItemDetailView(DetailView):
    model = Item
    template_name = 'product_detail.html'


class CheckoutView(View):
    def get(self, *args, **kwargs):
        #form
        form = CheckoutForm()

        return render(self.request, 'checkout.html', {'form':form})

    def post(self, *args, **kwargs):
        #form
        form = CheckoutForm(self.request.POST or None)
        if form.is_valid():
            print(form.cleaned_data)
            print("The form is valid")
            return redirect('checkout')
    

# Add To Cart View

@login_required
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
            return redirect('order-summary')
        else:

            order.items.add(order_item)
            messages.info(request, "This item was added to your cart.")
            return redirect('order-summary')
    else:
        order = Order.objects.create(
            user=request.user, ordered_date=ordered_date)
        order.item.add(order_item)
        messages.info(request, "This item was added to your cart.")
        return redirect('order-summary')
    return redirect('order-summary')

# Remove from Cart View

@login_required
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
            return redirect('order-summary')
        else:
            messages.info(request, "The item was was not in your cart.")
            return redirect('order-summary')
    else:
        messages.info(request, "You do not have an active order.")
        return redirect('order-summary')

    return redirect('order-summary')


@login_required
def remove_single_item_from_cart(request, slug):
    item = get_object_or_404(Item, slug=slug)
    order_qs = Order.objects.filter(user=request.user, ordered=False)
    # Check if the order exists
    if order_qs.exists():
        order = order_qs[0]

    # Check if order item is in the order
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item, user=request.user, ordered=False)[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
            
            
            messages.info(request, "This item quantity was updated.")
            return redirect('order-summary')
        else:
            messages.info(request, "The item was was not in your cart.")
            return redirect('order-summary')
    else:
        messages.info(request, "You do not have an active order.")
        return redirect('order-summary')

    return redirect('order-summary')
