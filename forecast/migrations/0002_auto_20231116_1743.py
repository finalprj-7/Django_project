# Generated by Django 3.1.1 on 2023-11-16 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='weather',
            name='description',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='humidity',
        ),
        migrations.RemoveField(
            model_name='weather',
            name='temperature',
        ),
        migrations.AddField(
            model_name='weather',
            name='base_date',
            field=models.CharField(default='20231116', max_length=8),
        ),
        migrations.AddField(
            model_name='weather',
            name='base_time',
            field=models.CharField(default='0000', max_length=4),
        ),
        migrations.AddField(
            model_name='weather',
            name='category',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='weather',
            name='fcst_date',
            field=models.CharField(default='20231116', max_length=8),
        ),
        migrations.AddField(
            model_name='weather',
            name='fcst_time',
            field=models.CharField(default='0000', max_length=4),
        ),
        migrations.AddField(
            model_name='weather',
            name='fcst_value',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AddField(
            model_name='weather',
            name='nx',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='weather',
            name='ny',
            field=models.IntegerField(default=0),
        ),
    ]
