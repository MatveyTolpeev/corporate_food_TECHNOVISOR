# Generated by Django 4.2.1 on 2023-05-09 07:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate_food', '0006_remove_employee_time_end_work_alter_order_end_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='time_end_work',
            field=models.TimeField(default=datetime.time(19, 0)),
        ),
        migrations.AlterField(
            model_name='order',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 9, 13, 19, 24, 549392)),
        ),
    ]
