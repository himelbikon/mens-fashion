from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView


class LatestProducts(APIView):
    def get(self, request):
        products = Product.objects.all()[0:8]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class SingleProduct(APIView):
    def get(self, request, pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
