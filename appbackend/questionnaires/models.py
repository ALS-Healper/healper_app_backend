from datetime import timezone, datetime
from django.db import models
from users.models import Therapist, Client

class Questionnaire(models.Model):
    title = models.CharField(null=True, blank=True, max_length=100)
    creator = models.ForeignKey(Therapist, on_delete=models.CASCADE)

class QuestionnaireEntry(models.Model):
    creator = models.ForeignKey(Client, on_delete=models.CASCADE)
    questionnaire = models.ForeignKey(Questionnaire, null=True, on_delete=models.SET_NULL)
    entry_date = models.DateTimeField(default=datetime.now())
    is_completed = models.BooleanField(default=False)


class Question(models.Model):
    #questionnaires = models.ManyToManyField(Questionnaire, related_name="questions")
    question_text = models.CharField(max_length=250)
    creator = models.ForeignKey(Therapist, on_delete=models.CASCADE)
    #question_type = models.CharField(max_length=20)

#question type choices
class QuestionChoice(Question):
    questionnaires = models.ManyToManyField(Questionnaire, related_name="choicequestions")

class OptionChoice(models.Model):
    question = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE, related_name="optionchoices")
    option_value = models.CharField(null=False, blank=False, max_length=75)

#question type input
class QuestionInput(Question):
    questionnaires = models.ManyToManyField(Questionnaire, related_name="inputquestions")

class OptionInput(models.Model):
    question = models.ForeignKey(QuestionInput, on_delete=models.CASCADE, related_name="optioninputs")
    standard_text = models.CharField(default="Enter answer here", max_length=75)

#question type numeric
class QuestionNumeric(Question):
    questionnaires = models.ManyToManyField(Questionnaire, related_name="numericquestions")

class OptionNumeric(models.Model):
    question = models.ForeignKey(QuestionNumeric, on_delete=models.CASCADE, related_name="optionnumerics")
    min_value = models.IntegerField(default=1)
    max_value = models.IntegerField(default=10)

class QuestionInputEntry(models.Model):
    question = models.ForeignKey(QuestionInput, on_delete=models.CASCADE, related_name="inputentries")
    questionnaire_entry = models.ForeignKey(QuestionnaireEntry, on_delete=models.CASCADE, related_name="inputentries")
    response_text = models.CharField(max_length=300)
    entry_date = models.DateTimeField(default=datetime.now())
    creator = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="inputentries")

class QuestionNumericEntry(models.Model):
    question = models.ForeignKey(QuestionNumeric, on_delete=models.CASCADE, related_name="numericentries")
    questionnaire_entry = models.ForeignKey(QuestionnaireEntry, on_delete=models.CASCADE, related_name="numericentries")
    response_value = models.IntegerField()
    entry_date = models.DateTimeField(default=datetime.now())
    creator = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="numericentries")

class QuestionChoiceEntry(models.Model):
    question = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE, related_name="choiceentries")
    questionnaire_entry = models.ForeignKey(QuestionnaireEntry, on_delete=models.CASCADE, related_name="choiceentries")
    choice_value = models.CharField(max_length=100)
    entry_date = models.DateTimeField(default=datetime.now())
    creator = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="choiceentries")

