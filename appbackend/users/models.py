from django.db import models
from django.contrib.auth.models import User


class Therapist(models.Model):
    is_therapist = models.BooleanField(default=True)
    user_ref = models.ForeignKey(User, on_delete=models.CASCADE)

class Client(models.Model):
    thera = models.ForeignKey(Therapist, null=True, blank=True, on_delete=models.SET_NULL)
    user_ref = models.ForeignKey(User, on_delete=models.CASCADE)
     
  