# Generated by Django 4.2.1 on 2023-05-10 10:16

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corporate_food', '0010_order_comment_alter_order_end_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='end_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 10, 16, 16, 19, 744576)),
        ),
    ]
