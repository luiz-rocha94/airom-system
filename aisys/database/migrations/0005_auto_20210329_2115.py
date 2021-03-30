# Generated by Django 3.1.7 on 2021-03-30 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0004_auto_20210329_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heartfailure',
            name='anaemia',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='heartfailure',
            name='death_event',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='heartfailure',
            name='diabetes',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='heartfailure',
            name='high_blood_pressure',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='heartfailure',
            name='sex',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='heartfailure',
            name='smoking',
            field=models.IntegerField(),
        ),
    ]