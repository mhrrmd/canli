# Generated by Django 4.2.5 on 2023-10-17 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizsorulari',
            name='dogru_secenek',
            field=models.CharField(choices=[('secenek1', 'Secenek 1'), ('secenek2', 'Secenek 2'), ('secenek3', 'Secenek 3'), ('secenek4', 'Secenek 4')], max_length=255),
        ),
    ]