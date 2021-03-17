from datetime import date

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

COLOR_FAMILY = (
    ("White", "White"),
    ("Black", "Black"),
    ("Grey", "Grey"),
    ("Red", "Red"),
    ("Blue", "Blue"),
    ("Yellow", "Yellow"),
    ("Cyan", "Cyan"),
    ("Green", "Green"),
    ("Silver", "Silver"),
    ("Gold", "Gold"),
    ("Orange", "Orange"),
    ("Purple", "Purple"),
)


class Product(models.Model):
    title = models.CharField(max_length=200, unique=True)
    description = models.TextField()
    category = models.ForeignKey('categorys.Category', on_delete=models.DO_NOTHING, null=True, blank=True)
    brand = models.ForeignKey('categorys.Brand', on_delete=models.DO_NOTHING, null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20)
    rating = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to="product_images/%Y/%m/%d")
    visible = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=500)
    cash_on_delivery = models.BooleanField(default=False)
    free_shipping = models.BooleanField(default=False)
    warranty_years = models.PositiveIntegerField(default=0)
    discount_price = models.DecimalField(decimal_places=2, max_digits=20, null=True, blank=True)
    discount_expiry = models.DateTimeField(null=True, blank=True)
    color_family=models.CharField(choices=COLOR_FAMILY,null=True,blank=True, max_length=10)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
