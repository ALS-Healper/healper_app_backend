from django.shortcuts import render

from rest_framework import viewsets, permissions, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import NotificationSerializer
from .models import Notification, Interval


class NotificationViewSet(viewsets.ModelViewSet):

    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
