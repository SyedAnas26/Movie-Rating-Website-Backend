# Generated by Django 3.1.3 on 2020-11-22 13:19

from django.db import migrations

from script.load_movies import load_data


class Migration(migrations.Migration):
    dependencies = [
        ('DjangoBackEnd', '0002_auto_20201118_2200'),
    ]

    operations = [
        migrations.RunPython(load_data)
    ]