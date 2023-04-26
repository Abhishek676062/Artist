from django.contrib.auth.models import User
from rest_framework import serializers
from myapp.models import Work

class WorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = ['id', 'link', 'work_type', 'artist']

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User
        fields = ['username', 'password']
