from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    image = models.ImageField(upload_to='menu/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='foods')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
