from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import *

class CustomUserCreateSerializer(UserCreateSerializer):
    class Meta(UserSerializer.Meta):
        model = User
        field = ('id', 'email', 'username', 'password', 'first_name', 'last_name', 'isRider' )