# Generated by Django 3.1.3 on 2020-11-16 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('MovieId', models.AutoField(primary_key=True, serialize=False)),
                ('MovieTitle', models.CharField(max_length=100)),
                ('ReleaseDate', models.DateField()),
                ('MovieImage', models.ImageField(upload_to='media')),
            ],
            options={
                'verbose_name': 'Movie',
                'verbose_name_plural': 'Movies',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UpVotes', models.BigIntegerField()),
                ('DownVotes', models.BigIntegerField()),
                ('Rating', models.FloatField()),
                ('MovieId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='DjangoBackEnd.movie')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
    ]