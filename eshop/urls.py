from django.urls import path
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('product_info/', views.productinfo, name='product-info'),
    path('cart/', views.cart, name = 'cart'),
    path('checkout/', views.checkout, name = 'checkout')
    


]
