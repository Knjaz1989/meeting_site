from rest_framework import serializers
from application.models import User


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {'password': {'write_only': True},
                        "is_superuser":  {'read_only': True},
                        "is_staff": {'read_only': True},
                        "is_active": {'read_only': True},
                        "date_joined": {'read_only': True},
                        "groups": {'read_only': True},
                        "user_permissions": {'read_only': True},
                        "last_login": {'read_only': True},
                        }
