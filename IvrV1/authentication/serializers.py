# serializers.py

from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'dob', 'doa', 'password']
        extra_kwargs = {'password': {'write_only': True}}

class AuthSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    dob = serializers.DateField()
    doa = serializers.DateField()
