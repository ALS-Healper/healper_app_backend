from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions
from drf_multiple_model.views import ObjectMultipleModelAPIView

from questionnaires.models import Questionnaire, Question, QuestionInputEntry, QuestionChoiceEntry, QuestionNumericEntry
from .serializers import ClientEntrySerializer, QuestionChoiceEntrySerializer, QuestionEntrySerializer, QuestionInputEntrySerializer, QuestionNumericEntrySerializer, UserSerializer, GroupSerializer, QuestionnaireSerializer, QuestionSerializer
from users.models import Client
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


class QuestionInputEntryViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionInputEntrySerializer
    queryset = QuestionInputEntry.objects.all()


class QuestionChoiceEntryViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionChoiceEntrySerializer
    queryset = QuestionChoiceEntry.objects.all()


class QuestionNumericEntryViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionNumericEntrySerializer
    queryset = QuestionNumericEntry.objects.all()



class ClientEntryViewSet(viewsets.ModelViewSet):
    serializer_class = ClientEntrySerializer
    queryset = Client.objects.all()