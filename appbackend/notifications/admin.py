from django.contrib import admin
from .models import Notification, Interval

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ["title", "text"]

@admin.register(Interval)
class IntervalAdmin(admin.ModelAdmin):
    list_display = ["interval_type", "separation_count", "max_numb_occurrences", "time_of_day", "day_of_week", "day_of_month", "week_of_month", "month_of_year"]