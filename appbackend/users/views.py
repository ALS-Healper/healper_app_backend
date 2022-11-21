from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, GroupSerializer, TherapistSerializer, ClientSerializer
from .models import Client, Therapist


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that either gives access to view or edit a user
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that either gives access to view or edit a group
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class UserDetailViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query = User.objects.filter(pk = self.request.user.pk)
        return query


