# Generated by Django 2.1 on 2019-04-22 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20190422_1616'),
    ]

    operations = [
        migrations.AddField(
            model_name='hot_daily',
            name='update_time',
            field=models.DateField(auto_now=True),
        ),
    ]
