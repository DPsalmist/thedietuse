# Generated by Django 3.2.6 on 2022-10-15 19:34

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_auto_20221015_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalappraisal',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 20, 34, 9, 849742)),
        ),
        migrations.AlterField(
            model_name='jobappraisal',
            name='appraisal_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 20, 34, 9, 849742)),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 20, 34, 9, 853333)),
        ),
        migrations.AlterField(
            model_name='report',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 20, 34, 9, 849742)),
        ),
        migrations.AlterField(
            model_name='staffappraisal',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 20, 34, 9, 849742)),
        ),
    ]
