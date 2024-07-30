from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Alert

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class AlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alert
        fields = ['id', 'cryptocurrency', 'target_price', 'created_at', 'triggered_at', 'status']
