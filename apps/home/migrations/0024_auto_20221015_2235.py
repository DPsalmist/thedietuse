# Generated by Django 3.2.6 on 2022-10-15 22:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0023_auto_20221015_2036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='generalappraisal',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 23, 35, 2, 928259)),
        ),
        migrations.AlterField(
            model_name='jobappraisal',
            name='appraisal_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 23, 35, 2, 928259)),
        ),
        migrations.AlterField(
            model_name='project',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 23, 35, 2, 933123)),
        ),
        migrations.AlterField(
            model_name='report',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 23, 35, 2, 928259)),
        ),
        migrations.AlterField(
            model_name='staffappraisal',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 15, 23, 35, 2, 928259)),
        ),
    ]
