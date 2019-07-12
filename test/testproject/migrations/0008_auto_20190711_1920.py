# Generated by Django 2.1.7 on 2019-07-11 16:20

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testproject', '0007_auto_20190710_1916'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groups',
            name='description',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='groups',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='users',
            name='created',
            field=models.DateField(default=datetime.datetime(2019, 7, 11, 19, 20, 49, 841725)),
        ),
        migrations.AlterField(
            model_name='users',
            name='group',
            field=models.ForeignKey(choices=[(2, 'Red'), (3, 'Blue'), (7, 'blabla'), (8, 'Pinks')], on_delete=django.db.models.deletion.CASCADE, to='testproject.Groups'),
        ),
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]