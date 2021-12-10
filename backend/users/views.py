from django.utils.timezone import utc
import random
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import APIException
from rest_framework.permissions import IsAuthenticated
from methods import send_mail
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
        if request.user.is_authenticated:
            raise APIException('User already registered!')

        data = request.data
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class EamailConfirmationAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        pass

    def get(self, request):
        if request.user.email_confirmed:
            raise APIException('User already confirmed email!')

        now = datetime.utcnow().replace(tzinfo=utc)

        seconds = (
            now - EmailConfirmation.objects.all().first().created_at).total_seconds()

        # email_confirmation = EmailConfirmation(
        #     user=request.user,
        #     code=''.join(
        #         [random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789') for _ in range(6)])
        # )
        # email_confirmation.save()
        return Response({'ok': int(seconds)})


class AllUsers(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
