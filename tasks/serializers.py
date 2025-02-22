# tasks/serializers.py
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ('user',)  # Ensures that the 'user' field is automatically populated and not editable

class UserRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Ensures password is not returned in the response

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        user.is_active = False
        user.save()
        return user