# Generated by Django 4.2.7 on 2023-11-25 20:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0007_remove_rentedbooks_date_rentedbooks_datea'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rentedbooks',
            name='datea',
        ),
        migrations.AddField(
            model_name='rentedbooks',
            name='date',
            field=models.DateField(default=datetime.datetime(2023, 11, 25, 20, 29, 6, 19393, tzinfo=datetime.timezone.utc)),
        ),
    ]
