# Generated by Django 3.1.7 on 2021-02-26 06:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0006_rating_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rating',
            name='user_id',
        ),
    ]