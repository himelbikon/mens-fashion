from django.utils.timezone import utc
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from methods import send_email
from .models import *
from .serializers import *
from datetime import datetime


class Profile(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
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
        user = User.objects.filter(email=request.data['email']).first()

        if request.user.is_authenticated or user:
            raise APIException('User already registered!')

        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class AllUsers(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    # def code(self):
    #     string = 'QWERTYUIOPLKJHGFDSAZXCVBNM1234567890'
    #     return ''.join([random.choice(string) for _ in range(6)])

        # now = datetime.utcnow().replace(tzinfo=utc)

        # seconds = (
        #     now - EmailConfirmation.objects.all().first().created_at).total_seconds()
