# Generated by Django 2.2.14 on 2021-09-25 03:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0038_imageuploadadmin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dentistprofile',
            old_name='Address1',
            new_name='Address',
        ),
        migrations.RemoveField(
            model_name='dentistprofile',
            name='Address2',
        ),
        migrations.RemoveField(
            model_name='dentistprofile',
            name='City',
        ),
        migrations.RemoveField(
            model_name='dentistprofile',
            name='Clinic',
        ),
        migrations.RemoveField(
            model_name='dentistprofile',
            name='Country',
        ),
        migrations.RemoveField(
            model_name='dentistprofile',
            name='Postcode',
        ),
    ]
