# Generated by Django 4.2.7 on 2023-11-25 20:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0005_rentedbooks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rentedbooks',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 11, 25, 17, 25, 49, 464521)),
        ),
    ]