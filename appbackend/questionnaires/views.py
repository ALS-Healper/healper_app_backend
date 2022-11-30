from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from questionnaires.models import Questionnaire, Question, QuestionInput,QuestionChoice,QuestionNumeric, QuestionInputEntry, QuestionChoiceEntry, QuestionNumericEntry
from .serializers import ClientEntrySerializer, QuestionChoiceEntrySerializer, QuestionChoiceSerializer, QuestionEntrySerializer, QuestionInputEntrySerializer, QuestionInputSerializer, QuestionNumericEntrySerializer, QuestionNumericSerializer, UserSerializer, QuestionnaireSerializer, QuestionSerializer
from users.models import Client

class QuestionnaireViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionnaireSerializer
    queryset = Questionnaire.objects.all()
    

class QuestionViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer
    queryset = Question.objects.all()

class QuestionInputViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionInputSerializer
    queryset = QuestionInput.objects.all()

class QuestionChoiceViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionChoiceSerializer
    queryset = QuestionChoice.objects.all()

class QuestionNumericViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionNumericSerializer
    queryset = QuestionNumeric.objects.all()


class QuestionInputEntryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionInputEntrySerializer
    queryset = QuestionInputEntry.objects.all()


class QuestionChoiceEntryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionChoiceEntrySerializer
    queryset = QuestionChoiceEntry.objects.all()


class QuestionNumericEntryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionNumericEntrySerializer
    queryset = QuestionNumericEntry.objects.all()


class ClientEntryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    serializer_class = ClientEntrySerializer

    def get_queryset(self):
        client_pk = self.request.query_params.get("client_pk")
        if client_pk == self.request.user.pk:
            res = Client.objects.filter(pk = self.request.user.pk)
        else:
            res = Client.objects.filter(pk=client_pk, thera__pk=self.request.user.pk, data_access=True)
        return res