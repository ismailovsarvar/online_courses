# Generated by Django 5.0.6 on 2024-07-31 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bloglist',
            name='slug',
            field=models.SlugField(blank=True, unique=True),
        ),
    ]
