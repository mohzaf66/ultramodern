# Generated by Django 2.2.14 on 2021-09-14 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0032_auto_20210914_0422'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientproposedtreatment',
            name='Note',
        ),
        migrations.AlterField(
            model_name='patient',
            name='DentistNote',
            field=models.TextField(default='No Note Added'),
        ),
    ]