from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime


class Interval(models.Model):
    class IntervalTypes(models.TextChoices):
        DAILY = 'day'
        HOURLY = 'hour'
        MINUTELY = 'minute'
        MONTHLY = 'month'
        QUARTERLY = 'quarter'
        SECONDLY = 'second'
        WEEKLY = 'week'
        YEARLY = 'year'

    interval_type = models.CharField(choices=IntervalTypes.choices, default=IntervalTypes.DAILY, max_length=7, null=False)
    separation_count = models.IntegerField(default=0, null=True, blank=True)
    max_numb_occurrences = models.IntegerField(null=True, blank=True)
    time_of_day = models.TimeField(default=datetime.now().time(), null=False)
    day_of_week = models.IntegerField(null=True, blank=True, validators=([MinValueValidator(1), MaxValueValidator(7)]))
    day_of_month = models.IntegerField(null=True, blank=True, validators=([MinValueValidator(1), MaxValueValidator(31)]))
    week_of_month = models.IntegerField(null=True, blank=True, validators=([MinValueValidator(1), MaxValueValidator(5)]))
    month_of_year = models.IntegerField(null=True, blank=True, validators=([MinValueValidator(1), MaxValueValidator(12)]))

class Notification(models.Model):
    title = models.CharField(default="Healper", max_length=12)
    text = models.CharField(default="Healper notification", max_length=30)
    interval = models.ForeignKey(Interval, null=True, related_name="notification", on_delete=models.SET_NULL)