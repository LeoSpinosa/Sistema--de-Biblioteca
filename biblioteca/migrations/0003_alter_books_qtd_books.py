# Generated by Django 4.2.7 on 2023-11-25 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('biblioteca', '0002_alter_books_options_alter_genders_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='qtd_books',
            field=models.IntegerField(default=0),
        ),
    ]
