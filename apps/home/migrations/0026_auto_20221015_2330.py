# Generated by Django 3.2.6 on 2022-10-15 23:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0025_auto_20221015_2325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staffappraisal',
            name='staff_gender',
        ),
        migrations.AlterField(
            model_name='generalappraisal',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 16, 0, 30, 13, 327267)),
        ),
        migrations.AlterField(
            model_name='jobappraisal',
            name='appraisal_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 16, 0, 30, 13, 327267)),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 16, 0, 30, 13, 330666)),
        ),
        migrations.AlterField(
            model_name='report',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 16, 0, 30, 13, 327267)),
        ),
        migrations.AlterField(
            model_name='staffappraisal',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 16, 0, 30, 13, 327267)),
        ),
    ]
