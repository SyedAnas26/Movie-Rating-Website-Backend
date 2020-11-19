# Generated by Django 3.1.3 on 2020-11-18 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoBackEnd', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movierating',
            name='DownVotes',
            field=models.BigIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='movierating',
            name='Rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=5),
        ),
        migrations.AlterField(
            model_name='movierating',
            name='UpVotes',
            field=models.BigIntegerField(default=0),
        ),
    ]