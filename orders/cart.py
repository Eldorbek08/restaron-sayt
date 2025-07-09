from menu.models import FoodItem

class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart'] = {}
        self.cart = cart

    def add(self, food_id, quantity=1):
        food_id = str(food_id)
        if food_id in self.cart:
            self.cart[food_id] += quantity
        else:
            self.cart[food_id] = quantity
        self.save()

    def remove(self, food_id):
        food_id = str(food_id)
        if food_id in self.cart:
            del self.cart[food_id]
        self.save()

    def save(self):
        self.session.modified = True

    def clear(self):
        self.session['cart'] = {}
        self.save()

    def get_items(self):
        items = []
        for food_id, qty in self.cart.items():
            try:
                food = FoodItem.objects.get(id=food_id)
                items.append({
                    'food': food,
                    'quantity': qty,
                    'total': food.price * qty
                })
            except:
                pass
        return items

    def get_total(self):
        return sum(item['total'] for item in self.get_items())
