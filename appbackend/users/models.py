from django.db import models
from django.contrib.auth.models import User



class Therapist(models.Model):
    is_therapist = models.BooleanField(default=True)
    user_ref = models.ForeignKey(User, on_delete=models.CASCADE, related_name="therapist")

class Client(models.Model):
    thera = models.ForeignKey(Therapist, null=True, blank=True, on_delete=models.SET_NULL, related_name="clients")
    data_access = models.BooleanField(null=False, blank=False, default=True)
    user_ref = models.ForeignKey(User, on_delete=models.CASCADE, related_name="client")
    img_url = models.CharField(max_length=400, null=True)
     
  