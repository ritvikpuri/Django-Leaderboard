# Generated by Django 3.2.19 on 2023-06-09 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leaderboard_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Leaderboard',
            new_name='User',
        ),
    ]
