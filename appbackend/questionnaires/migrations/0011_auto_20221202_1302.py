# Generated by Django 3.2.15 on 2022-12-02 12:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0010_auto_20221202_1302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionchoiceentry',
            name='entry_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 2, 13, 2, 46, 393738)),
        ),
        migrations.AlterField(
            model_name='questioninputentry',
            name='entry_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 2, 13, 2, 46, 390735)),
        ),
        migrations.AlterField(
            model_name='questionnaireentry',
            name='entry_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 2, 13, 2, 46, 378739)),
        ),
        migrations.AlterField(
            model_name='questionnumericentry',
            name='entry_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 2, 13, 2, 46, 392738)),
        ),
    ]