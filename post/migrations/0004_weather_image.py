# Generated by Django 4.2.7 on 2023-11-27 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_remove_post_file_upload'),
    ]

    operations = [
        migrations.AddField(
            model_name='weather',
            name='image',
            field=models.ImageField(blank=True, upload_to='weather/images/'),
        ),
    ]
