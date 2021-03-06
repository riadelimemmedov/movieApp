# Generated by Django 3.2.9 on 2021-12-11 10:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20211211_0915'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=100, verbose_name='Yorum Yapan')),
                ('your_email', models.EmailField(max_length=254, verbose_name='Email')),
                ('text', models.TextField(max_length=500, verbose_name='Yorum')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='yorumlar', to='movies.movie')),
            ],
        ),
    ]
