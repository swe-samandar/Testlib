# Generated by Django 5.2 on 2025-04-20 09:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_test_end_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='is_basics',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='test',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2025, 4, 30, 9, 44, 19, 826333, tzinfo=datetime.timezone.utc)),
        ),
    ]
