# Generated by Django 4.2.7 on 2023-11-29 05:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0006_merge_0003_alter_weather_id_0005_choice_voters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='poll',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
