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


class ProductsOrderBy(APIView):
    def get(self, request):
        limit = int(request.GET.get('limit', 9))
        page = int(request.GET.get('page', 1))

        orderby = request.GET.get('orderby', None)
        category = request.GET.get('category', None)

        if orderby:
            products = Product.objects.all().order_by(
                '-' + orderby)[(page-1) * limit: page * limit]

        elif category:
            products = Product.objects.filter(category__slug=category)[
                (page-1) * limit: page * limit]

        else:
            products = Product.objects.all()[(page-1) * limit: page * limit]

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
