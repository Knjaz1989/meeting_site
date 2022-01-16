from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet
from application.models import User
from application.serializers import UserListSerializer


@permission_classes([IsAuthenticated])
class UserListViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_fields = ['gender', 'first_name', 'last_name']
    http_method_names = ['get']


class UserCreateViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    http_method_names = ['post']
