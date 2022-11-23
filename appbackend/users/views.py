from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from .serializers import UserSerializer, GroupSerializer, TherapistSerializer, ClientSerializer, ClientListSerializer, UserDetailSerializer
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
    serializer_class = UserDetailSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        query = User.objects.filter(pk = self.request.user.pk)
        return query


class TherapistDetailViewSet(viewsets.ModelViewSet):
    serializer_class = TherapistSerializer
    permission_classes = [IsAuthenticated]
    queryset = Therapist.objects.all()

class ClientDetailViewSet(viewsets.ModelViewSet):
    serializer_class = ClientSerializer
    permission_classes = [IsAuthenticated]
    queryset = Client.objects.all()

class TherapistClientListViewsSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ClientListSerializer

    def get_queryset(self):
        therapist = Therapist.objects.filter(user_ref__pk = self.request.user.pk)
        #query = Client.objects.filter(thera = therapist)
        return therapist
