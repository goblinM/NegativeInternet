# Generated by Django 2.1 on 2019-04-22 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_hot_daily'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_type',
            field=models.CharField(choices=[(0, 'user'), (1, 'admin')], default=0, max_length=25, verbose_name='用户的类型'),
        ),
    ]
