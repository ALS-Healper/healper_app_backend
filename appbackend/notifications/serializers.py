from notifications.models import Notification, Interval
from rest_framework import serializers

class IntervalSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Interval
        fields = ["interval_type", "separation_count", "max_numb_occurrences", "time_of_day", "day_of_week", "day_of_month", "week_of_month", "month_of_year"]

class NotificationSerializer(serializers.ModelSerializer):
    interval = IntervalSerializer(many=False)
    class Meta:
        model = Notification
        fields = ["title", "text", "interval"]