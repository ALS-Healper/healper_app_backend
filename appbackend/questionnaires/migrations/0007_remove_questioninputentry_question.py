# Generated by Django 3.2.15 on 2022-11-18 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questionnaires', '0006_auto_20221118_1044'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questioninputentry',
            name='question',
        ),
    ]
