# Generated by Django 4.0.4 on 2022-10-12 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('iteration3', '0004_alter_diaryentries_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary_menu',
            name='user',
        ),
        migrations.RemoveField(
            model_name='diaryentries',
            name='user',
        ),
    ]
