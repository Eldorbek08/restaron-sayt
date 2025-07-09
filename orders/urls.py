from django.urls import path
from .views import add_to_cart, remove_from_cart, cart_view

urlpatterns = [
    path('cart/', cart_view, name='cart'),
    path('add/<int:food_id>/', add_to_cart, name='add_to_cart'),
    path('remove/<int:food_id>/', remove_from_cart, name='remove_from_cart'),
]
