from django.urls import path
from .views import HomeView, ItemDetailView, add_to_cart,remove_from_cart

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('products/<slug>/', ItemDetailView.as_view(), name='products'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    


]
