# Generated by Django 3.2.15 on 2022-12-02 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_client_img_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='img_url',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
