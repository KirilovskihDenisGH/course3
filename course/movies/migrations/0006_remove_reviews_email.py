# Generated by Django 4.1.4 on 2022-12-14 07:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0005_remove_reviews_parent'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reviews',
            name='email',
        ),
    ]
