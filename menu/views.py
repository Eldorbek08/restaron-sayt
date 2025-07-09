from django.shortcuts import render
from .models import FoodItem, Category

def menu_list(request):
    categories = Category.objects.all()
    foods = FoodItem.objects.all()
    return render(request, 'menu/menu_list.html', {
        'categories': categories,
        'foods': foods,
    })
