from datetime import timezone
from django.db import models

from users.models import Therapist, Client


class Questionnaire(models.Model):
    title = models.CharField(null=True, blank=True, max_length=100)
    creator = models.ForeignKey(Therapist, on_delete=models.CASCADE)


class Question(models.Model):
    questionnaires = models.ManyToManyField(Questionnaire, related_name="questions")
    question_text = models.CharField(max_length=250)
    creator = models.ForeignKey(Therapist, on_delete=models.CASCADE)


class QuestionEntry(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    response_text = models.CharField(max_length=300)
    entry_date = models.DateTimeField(auto_now_add=True)
    creator = models.ForeignKey(Client, on_delete=models.CASCADE)
