from rest_framework import serializers
from application.models import User


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        exclude = ['password']
