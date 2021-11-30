from .models import *
from rest_framework import serializers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'category',
            'category_name',
            'views',
            'details',
            'image',
            'image2',
            'image3',
            'image4',
            'image5',
        ]

    # extra_kwargs = {'ratings': {'write_only': True}}


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image']


class ShowcaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showcase
        fields = ['id', 'name',  'details', 'product_id', 'image']
