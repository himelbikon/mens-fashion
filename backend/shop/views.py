from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView


class SingleProduct(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class LatestProducts(APIView):
    def get(self, request, limit=None):
        products = Product.objects.all()[0:8]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class PopularProducts(APIView):
    def get(self, request, limit=None):
        products = Product.objects.all().order_by('-view')[0:8]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
