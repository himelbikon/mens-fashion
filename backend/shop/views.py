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
    def get(self, request, limit, page):
        products = Product.objects.all()[(page-1) * limit: page * limit]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class PopularProducts(APIView):
    def get(self, request, limit, page):
        products = Product.objects.all().order_by(
            '-views')[(page-1) * limit: page * limit]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class Categories(APIView):
    def get(self, request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)


class Showcases(APIView):
    def get(self, request):
        products = Showcase.objects.all()
        serializer = ShowcaseSerializer(products, many=True)
        return Response(serializer.data)
