# Generated by Django 3.2.9 on 2021-12-11 04:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0006_auto_20211201_1754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='image_cover',
            field=models.ImageField(upload_to='movies', verbose_name='Film ArkaPlan Resmi'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='image_name',
            field=models.ImageField(upload_to='movies', verbose_name='Film On Resim'),
        ),
    ]