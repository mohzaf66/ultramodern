# Generated by Django 2.2.14 on 2021-09-05 11:32

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolioApp', '0010_auto_20210905_1125'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Patient_Proposed_Treatment',
            new_name='PatientProposedTreatment',
        ),
    ]
