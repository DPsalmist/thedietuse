# Generated by Django 3.1.7 on 2022-09-09 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_auto_20220909_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='foodorder',
            name='date_needed',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
