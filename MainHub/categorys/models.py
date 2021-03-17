from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Primarycategory(models.Model):
    title = models.CharField(max_length=500, unique=True)
    visible = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Secondarycategory(models.Model):
    title = models.CharField(max_length=500, unique=True)
    visible = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    primary_category = models.ForeignKey(Primarycategory, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=500, unique=True)
    visible = models.BooleanField(default=False)
    secondary_category = models.ForeignKey(Secondarycategory, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Brand(models.Model):
    title = models.CharField(max_length=500, unique=True)
    visible = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
