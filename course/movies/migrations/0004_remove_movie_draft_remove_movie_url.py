# Generated by Django 4.1.3 on 2022-12-13 01:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_remove_movie_format_alter_movie_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movie',
            name='draft',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='url',
        ),
    ]