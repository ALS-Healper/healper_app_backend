from django.contrib import admin
from questionnaires.models import QuestionChoiceEntry, QuestionInputEntry, QuestionNumericEntry, QuestionnaireEntry
from questionnaires.models import Question, Questionnaire, QuestionChoice, QuestionInput, QuestionNumeric, OptionChoice, OptionInput, OptionNumeric

# Register your models here.
@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    list_display = ['creator', 'title']

@admin.register(QuestionnaireEntry)
class QuestionnaireEntryAdmin(admin.ModelAdmin):
    list_display = ['creator', 'entry_date']

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['creator', 'question_text', 'get_questionnaires']

    #find all questionnaires the question is part of
    def get_questionnaires(self, obj):
        return "\n".join([p.title for p in obj.questionnaires.all()])

@admin.register(QuestionInputEntry)
class QuestionEntryAdmin(admin.ModelAdmin):
   list_display = ['creator', 'get_question_text', 'response_text', 'entry_date']
   
# To display the question text in list view
   def get_question_text(self, obj):
      return obj.question.question_text

@admin.register(QuestionChoiceEntry)
class QuestionEntryAdmin(admin.ModelAdmin):
   list_display = ['creator', 'get_question_text', 'choice_value', 'entry_date']
# To display the question text in list view
   def get_question_text(self, obj):
      return obj.question.question_text

@admin.register(QuestionNumericEntry)
class QuestionEntryAdmin(admin.ModelAdmin):
   list_display = ['creator', 'get_question_text', 'response_value', 'entry_date']
# To display the question text in list view
   def get_question_text(self, obj):
      return obj.question.question_text


@admin.register(QuestionInput)
class QuestionInputAdmin(admin.ModelAdmin):
   list_display = ['pk','creator', 'question_text', 'get_questionnaires']

   #find all questionnaires the question is part of
   def get_questionnaires(self, obj):
      return "\n".join([p.title for p in obj.questionnaires.all()])

@admin.register(QuestionChoice)
class QuestionChoiceAdmin(admin.ModelAdmin):
   list_display = ['pk','creator', 'question_text', 'get_questionnaires']

   #find all questionnaires the question is part of
   def get_questionnaires(self, obj):
      return "\n".join([p.title for p in obj.questionnaires.all()])

@admin.register(QuestionNumeric)
class QuestionNumericAdmin(admin.ModelAdmin):
   list_display = ['pk','creator', 'question_text', 'get_questionnaires']

   #find all questionnaires the question is part of
   def get_questionnaires(self, obj):
      return "\n".join([p.title for p in obj.questionnaires.all()])


@admin.register(OptionInput)
class OptionInputAdmin(admin.ModelAdmin):
   pass

@admin.register(OptionChoice)
class OptionChoiceAdmin(admin.ModelAdmin):
   pass

@admin.register(OptionNumeric)
class OptionNumericAdmin(admin.ModelAdmin):
   pass