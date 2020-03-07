from django.urls import path
from . import views
from cart.views import add_to_cart, remove_from_cart

urlpatterns = [
    path('', views.Home.as_view(), name='index'),
    path('cart/<slug>/', views.add_to_cart, name='cart'),
    path('remove/<slug>/', views.remove_from_cart, name='remove-cart')


]