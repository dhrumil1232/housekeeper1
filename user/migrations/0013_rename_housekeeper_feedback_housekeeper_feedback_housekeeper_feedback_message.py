# Generated by Django 4.0.3 on 2022-04-19 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0012_rename_feedback_housekeeper_feedback_housekeeper_feedback_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='housekeeper_feedback',
            old_name='housekeeper_feedback',
            new_name='housekeeper_feedback_message',
        ),
    ]
