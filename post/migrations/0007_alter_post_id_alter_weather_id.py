# Generated by Django 4.2.7 on 2023-11-29 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_merge_20231129_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='weather',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
