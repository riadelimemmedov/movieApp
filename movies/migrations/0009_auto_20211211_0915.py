# Generated by Django 3.2.9 on 2021-12-11 05:15

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_alter_person_biography'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
        migrations.AlterField(
            model_name='person',
            name='biography',
            field=models.CharField(max_length=3000),
        ),
    ]
