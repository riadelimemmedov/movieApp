# Generated by Django 3.2.9 on 2021-12-01 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_alter_movie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='budget',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]