# Generated by Django 2.2.14 on 2021-09-09 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0026_patientproposedtreatment_threedviewproposed'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='InternalStatus',
            field=models.TextField(default='On', null=True),
        ),
    ]