# Generated by Django 3.1.13 on 2021-11-18 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projekt', '0015_delete_abgabesystem'),
    ]

    operations = [
        migrations.AlterField(
            model_name='umwandlung',
            name='wirkungsgrad',
            field=models.FloatField(),
        ),
    ]