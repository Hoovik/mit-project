# Generated by Django 5.1.3 on 2024-11-18 16:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startit_app', '0002_job_created_at_alter_job_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Дата и время создания'),
        ),
    ]
