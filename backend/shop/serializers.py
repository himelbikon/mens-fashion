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


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'image']


class ShowcaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Showcase
        fields = ['id', 'name',  'details', 'product_id', 'image']


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
        read_only_fields = ('order',)


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = [
            'id',
            'user',
            'first_name',
            'last_name',
            'email',
            'phone',
            'address',
            'zipcode',
            'place',
            'created_at',
            'paid_amount',
            'token',
            'delivered',
            'items'
        ]

    def create(self, validated_data):
        items = validated_data.pop('items')
        order = Order.objects.create(**validated_data)

        for item in items:
            OrderItem.objects.create(**item, order=order)

        return order
