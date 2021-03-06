# Generated by Django 4.0.3 on 2022-04-18 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_housekeeper_notification_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Housekeeper_Leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('status', models.IntegerField(default=0, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('housekeeper_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.housekeeper')),
            ],
        ),
    ]
