# Generated by Django 3.1.7 on 2021-03-04 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0012_auto_20210304_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='condition',
            name='doctor_id',
        ),
        migrations.RemoveField(
            model_name='procedures',
            name='doctor_id',
        ),
    ]