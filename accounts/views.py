from django.shortcuts import render
from .models import Users
from .serializers import (UserSerializer)

from rest_framework import (viewsets, status, mixins)
from rest_framework.response import Response
from rest_framework.filters import SearchFilter

from django_filters.rest_framework import DjangoFilterBackend

# Create your views here.

class UserProfile(viewsets.GenericViewSet, mixins.ListModelMixin):
    """ Create , Updates, Retrieves and List User Account"""
    queryset = Users.objects.all()
    # serializers = {
    #     'default': UserSerializer,
    #     'list': UserSerializer,
    # }
    serializer_class = UserSerializer
    filter_backends = [DjangoFilterBackend]

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
