from django.shortcuts import render
from rest_framework import viewsets, mixins
from .Serializers import UserDetailSerializer
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.backends import BaseBackend
from django.db.models import Q
from django.contrib.auth import get_user_model
from .models import User


User = get_user_model()


class CustomBackend(BaseBackend):
    """
    custom user longin auther
    """
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = User.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None

class UserViewSet(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin):
    """
    user view set
    """
    queryset = User.objects.all()

    #Dynamic serializer
    def get_serializer_class(self):
        if self.action == 'retrieve':
            return UserDetailSerializer
        elif self.action == 'create':
            return UserDetailSerializer
        return UserDetailSerializer








