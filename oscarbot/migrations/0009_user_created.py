# Generated by Django 4.2.6 on 2024-07-18 21:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oscarbot', '0008_user_last_path_user_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='created',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name='Creation date'),
        ),
    ]
