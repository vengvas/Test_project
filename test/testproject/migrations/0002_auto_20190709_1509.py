# Generated by Django 2.1.7 on 2019-07-09 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testproject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='group',
            field=models.CharField(choices=[(1, 'Yellows'), (2, 'Red'), (3, 'Blue')], max_length=1),
        ),
    ]
