# Generated by Django 2.2 on 2020-07-30 13:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200730_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsitem',
            name='updated',
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 30, 14, 7, 21, 859089)),
        ),
    ]