# Generated by Django 3.2.15 on 2022-12-02 13:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0012_auto_20221202_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='questionchoiceentry',
            name='entry_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 2, 14, 6, 14, 786)),
        ),
        migrations.AlterField(
            model_name='questioninputentry',
            name='entry_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 2, 14, 6, 13, 998783)),
        ),
        migrations.AlterField(
            model_name='questionnaireentry',
            name='entry_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 2, 14, 6, 13, 991789)),
        ),
        migrations.AlterField(
            model_name='questionnumericentry',
            name='entry_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 2, 14, 6, 13, 999783)),
        ),
    ]