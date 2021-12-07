from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated


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


class OrdersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        orders = Order.objects.filter(user=request.user)
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        data['user'] = request.user.id
        serializer = OrderSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class OrderDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        order = Order.objects.get(pk=id)

        if request.user != order.user:
            raise exceptions.APIException('Invalid user!')

        serializer = OrderSerializer(order)
        return Response(serializer.data)
