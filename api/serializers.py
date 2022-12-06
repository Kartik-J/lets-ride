from rest_framework import serializers
from .models import *


class RiderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rider
        fields = '__all__'

class RequesterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requester
        
        fields = [field.name for field in model._meta.fields]
        fields.append('status')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        



    