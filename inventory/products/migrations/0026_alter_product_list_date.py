# Generated by Django 4.0.1 on 2022-01-19 19:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0025_alter_product_list_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 20, 1, 16, 41, 830506)),
        ),
    ]
