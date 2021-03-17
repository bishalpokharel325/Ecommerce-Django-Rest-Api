from rest_framework import serializers

from .models import Category, Primarycategory, Secondarycategory


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class PrimarycategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Primarycategory
        fields = "__all__"

class SecondarycategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Secondarycategory
        fields = "__all__"