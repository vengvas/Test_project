# Generated by Django 2.1.7 on 2019-07-10 13:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testproject', '0004_auto_20190710_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 10, 16, 51, 20, 955928)),
        ),
    ]
