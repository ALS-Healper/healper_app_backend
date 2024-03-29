# Generated by Django 3.2.15 on 2022-11-14 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_auto_20221114_1327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_text', models.CharField(max_length=250)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.therapist')),
            ],
        ),
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.therapist')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response_text', models.CharField(max_length=300)),
                ('entry_date', models.DateTimeField(auto_now_add=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.client')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='questionnaires.question')),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='quesionnaires',
            field=models.ManyToManyField(to='questionnaires.Questionnaire'),
        ),
    ]
