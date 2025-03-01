# Generated by Django 4.1.7 on 2023-12-07 12:47

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0011_enquiry_alter_announcement_time_alter_chats_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 7, 18, 17, 4, 145129)),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='course',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='student',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='chats',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 7, 18, 17, 4, 144274)),
        ),
    ]
