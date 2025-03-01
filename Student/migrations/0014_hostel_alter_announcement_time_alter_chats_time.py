# Generated by Django 4.1.7 on 2023-12-08 04:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0013_remove_attendance_student_attendance_student_id_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostelname', models.CharField(max_length=20)),
                ('seats', models.IntegerField()),
                ('room', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='announcement',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 10, 5, 57, 406155)),
        ),
        migrations.AlterField(
            model_name='chats',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 8, 10, 5, 57, 405333)),
        ),
    ]
