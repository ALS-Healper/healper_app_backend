from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from questionnaires.models import Questionnaire, Question, QuestionEntry
from .serializers import UserSerializer, GroupSerializer, QuestionnaireSerializer
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

    def get_queryset(self):
        #TODO: Fix this method once we start adding more questionnaires
        query   = Questionnaire.objects.filter(creator__user_ref=self.request.user)
        questions = Question.objects.filter(questionnaires__in=query)
        print(questions.first().questionnaires)
        for questionnaire in query:
            query.questions = questions
        return query