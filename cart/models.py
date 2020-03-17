from django.db import models
from django.conf import settings
from mamazon.models import Product

User = settings.AUTH_USER_MODEL

class Cart(models.Model):
    user = models.ForeignKey(User, null=True, black=True, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product, blank=True)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    created = models.DatetimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)