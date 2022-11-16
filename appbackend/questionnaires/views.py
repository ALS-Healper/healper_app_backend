from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from questionnaires.models import Questionnaire, Question, QuestionEntry
from .serializers import QuestionEntrySerializer, UserSerializer, GroupSerializer, QuestionnaireSerializer, QuestionSerializer
# Create your views here.

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


class QuestionnaireViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionnaireSerializer
    queryset = Questionnaire.objects.all()
    

class QuestionViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class QuestionEntryViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionEntrySerializer
    queryset = QuestionEntry.objects.all()