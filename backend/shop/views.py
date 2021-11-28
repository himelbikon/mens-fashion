from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView


class SingleProduct(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        product.views += 1
        product.save()
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class LatestProducts(APIView):
    def get(self, request, limit=None):
        if limit:
            products = Product.objects.all()[0:limit]
        else:
            products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class PopularProducts(APIView):
    def get(self, request, limit=None):
        if limit:
            products = Product.objects.all().order_by('-views')[0:limit]
        else:
            products = Product.objects.all().order_by('-views')
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class Categories(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        # products = Product.objects.all().order_by('-views')
        # serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
