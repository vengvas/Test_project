# Generated by Django 2.1.7 on 2019-07-10 13:47

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('testproject', '0003_auto_20190710_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 10, 13, 47, 5, 519239, tzinfo=utc)),
        ),
    ]
