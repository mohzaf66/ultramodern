# Generated by Django 2.2.14 on 2021-09-05 11:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolioApp', '0009_patient_proposed_treatment'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_proposed_treatment',
            name='Patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolioApp.Patient'),
        ),
        migrations.AlterField(
            model_name='patient_proposed_treatment',
            name='ProposedTreatment',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]