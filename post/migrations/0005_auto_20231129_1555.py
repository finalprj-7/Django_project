# Generated by Django 3.1.1 on 2023-11-29 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_weather_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
