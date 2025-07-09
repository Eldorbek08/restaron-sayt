from django.shortcuts import render, redirect
from .cart import Cart
from menu.models import FoodItem

def add_to_cart(request, food_id):
    cart = Cart(request)
    cart.add(food_id)
    return redirect('cart')

def remove_from_cart(request, food_id):
    cart = Cart(request)
    cart.remove(food_id)
    return redirect('cart')

def cart_view(request):
    cart = Cart(request)
    return render(request, 'orders/cart.html', {
        'items': cart.get_items(),
        'total': cart.get_total(),
    })
