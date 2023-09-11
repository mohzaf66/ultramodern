# Generated by Django 2.2.14 on 2021-09-18 03:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('portfolioApp', '0037_auto_20210917_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageUploadAdmin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image1', models.FileField(upload_to='')),
                ('Image2', models.FileField(upload_to='')),
                ('Image3', models.FileField(upload_to='')),
                ('Time', models.DateTimeField(auto_now_add=True, null=True)),
                ('Patient', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='portfolioApp.Patient')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
