# Generated by Django 4.0.4 on 2022-04-18 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_event_image_alter_event_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Specials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=200)),
                ('slug', models.SlugField(max_length=200)),
                ('description', models.TextField(db_index=True, max_length=500)),
                ('image', models.ImageField(blank=True, upload_to='specials/')),
            ],
            options={
                'ordering': ('name',),
                'index_together': {('id', 'slug')},
            },
        ),
    ]
