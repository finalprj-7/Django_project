# Generated by Django 4.2.7 on 2023-11-27 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_weather_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='head_image',
            field=models.ImageField(blank=True, upload_to='post/images/%Y/%m/%d/'),
        ),
    ]
