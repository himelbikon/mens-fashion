from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *


class Profile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # user = User.objects.get(pk=1)
        serializer = UserSerializer(request.user)
        return Response(serializer.data)

    def put(self, request):
        user = request.user
        serializer = UserSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class Subscribe(APIView):
    def post(self, request):
        serializer = SubscriptionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class Registration(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            raise APIException('User already registered!')

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        # serializer.save()
        return Response(serializer.data)
