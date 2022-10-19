# Generated by Django 3.2.6 on 2022-10-15 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stafff', '0005_profile_timeline'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(blank=True, default='media/default_profile_pic.jpeg', upload_to='profile_pics'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='timeline',
            field=models.ImageField(blank=True, default='media/default_profile_pic.jpeg', upload_to='timeline_pics/'),
        ),
    ]
