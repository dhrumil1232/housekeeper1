# Generated by Django 4.0.3 on 2022-04-17 14:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_housekeeper_notification'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Housekeeper_Notification',
        ),
    ]