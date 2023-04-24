from django.db import models
from django.db.models.deletion import CASCADE, SET_NULL
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class Product(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    price = models.IntegerField(default=0)
    explanation = models.TextField(max_length=300)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class OrderHistory(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=CASCADE,
        related_name="has_ordered"
    )
    product = models.ForeignKey(
        Product,
        on_delete=SET_NULL,
        null=True,
        related_name="product_history"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    price = models.IntegerField(default=0)
    num = models.IntegerField(default=1)

    def __str__(self):
        return f"<購入者:{self.user.username} 商品名: {self.product.name}>"