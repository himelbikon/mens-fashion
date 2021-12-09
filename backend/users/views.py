import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from methods import send_mail
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
    def post(self, request, token=None):
        if request.user.is_authenticated:
            raise APIException('User already registered!')

        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        self.register_email(data)
        return Response(serializer.data)

    def register_email(self, data):
        subject = data['email_subject']
        token = self.get_token()

        message = "Don't share this link with anyone \n" + f"/{token}/"

        send_mail(data['email'], subject, message)

    def get_token(self):
        return ''.join(
            [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(20)])
