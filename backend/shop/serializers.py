from .models import *
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

    extra_kwargs = {'ratings': {'write_only': True}}


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'image']


class ShowcaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showcase
        fields = ['id', 'name',  'details', 'product_id', 'image']
