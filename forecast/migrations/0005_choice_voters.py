# Generated by Django 3.1.1 on 2023-11-26 11:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forecast', '0004_auto_20231125_1858'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='voters',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
