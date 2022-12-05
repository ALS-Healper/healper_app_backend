from django.contrib import admin
from questionnaires.models import QuestionChoiceEntry, QuestionInputEntry, QuestionNumericEntry
from questionnaires.models import Question, Questionnaire, QuestionChoice, QuestionInput, QuestionNumeric, OptionChoice, OptionInput, OptionNumeric
from .models import Client, Therapist

@admin.register(Therapist)
class TherapistAdmin(admin.ModelAdmin):
   list_display = ['user_ref']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
   list_display = ['user_ref']


