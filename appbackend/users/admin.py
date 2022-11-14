from django.contrib import admin

from questionnaires.models import Question, QuestionEntry, Questionnaire
from .models import Client, Therapist

@admin.register(Therapist)
class TherapistAdmin(admin.ModelAdmin):
   list_display = ['user_ref']

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
   list_display = ['user_ref']


@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ['creator', 'title']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['creator', 'question_text', 'get_questionnaires']

    #find all questionnaires the question is part of
    def get_questionnaires(self, obj):
        return "\n".join([p.title for p in obj.questionnaires.all()])

@admin.register(QuestionEntry)
class QuestionEntryAdmin(admin.ModelAdmin):
   list_display = ['creator', 'get_question_text', 'response_text', 'entry_date']

# To display the question text in list view
   def get_question_text(self, obj):
    return obj.question.question_text