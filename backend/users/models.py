from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise valueError('User must have an email!')
        if not password:
            raise valueError('User must have an password!')

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        if not email:
            raise valueError('User must have an email!')
        if not password:
            raise valueError('User must have an password!')

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractUser):
    first_name = models.CharField(max_length=20, blank=True)
    last_name = models.CharField(max_length=20, blank=True)
    username = models.CharField(max_length=20, default='username')
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to='user/avatar/', blank=True, null=True)

    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Subscription(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


class Email(models.Model):
    address = models.EmailField()
    password = models.CharField(max_length=100)
    server = models.CharField(max_length=40)
    port = models.CharField(max_length=10)

    def __str__(self):
        return self.address
