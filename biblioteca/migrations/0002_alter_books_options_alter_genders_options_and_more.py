# Generated by Django 4.2.7 on 2023-11-11 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': 'Book', 'verbose_name_plural': 'Books'},
        ),
        migrations.AlterModelOptions(
            name='genders',
            options={'verbose_name': 'Gender', 'verbose_name_plural': 'Genders'},
        ),
        migrations.AddField(
            model_name='books',
            name='in_stock',
            field=models.BooleanField(default=False),
        ),
    ]
