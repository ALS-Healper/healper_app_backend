# Generated by Django 3.2.15 on 2022-12-02 13:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0012_alter_interval_time_of_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='interval',
            name='time_of_day',
            field=models.TimeField(default=datetime.time(14, 6, 14, 3788)),
        ),
    ]
