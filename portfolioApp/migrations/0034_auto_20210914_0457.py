# Generated by Django 2.2.14 on 2021-09-14 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0033_auto_20210914_0449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='AdminNote',
            field=models.TextField(default='Not Added'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='DentistNote',
            field=models.TextField(default='Not Added'),
        ),
    ]
