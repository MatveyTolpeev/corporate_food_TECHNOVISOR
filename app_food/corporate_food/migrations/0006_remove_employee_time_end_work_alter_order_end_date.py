# Generated by Django 4.2.1 on 2023-05-08 20:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate_food', '0005_alter_order_end_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='time_end_work',
        ),
        migrations.AlterField(
            model_name='order',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 2, 18, 12, 251815)),
        ),
    ]
