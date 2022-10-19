# Generated by Django 3.2.6 on 2022-10-15 19:25

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20221015_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalappraisal',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 20, 25, 6, 225355)),
        ),
        migrations.AlterField(
            model_name='jobappraisal',
            name='appraisal_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 20, 25, 6, 225355)),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 20, 25, 6, 228723)),
        ),
        migrations.AlterField(
            model_name='report',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 20, 25, 6, 225355)),
        ),
        migrations.AlterField(
            model_name='staffappraisal',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 20, 25, 6, 225355)),
        ),
        migrations.AlterField(
            model_name='staffappraisal',
            name='staff_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_appraisals', to=settings.AUTH_USER_MODEL),
        ),
    ]
