# Generated by Django 4.1.3 on 2022-11-29 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_interval_time_of_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interval',
            name='separation_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='interval',
            name='time_of_day',
            field=models.TimeField(default=datetime.time(16, 26, 8, 855864)),
        ),
    ]
