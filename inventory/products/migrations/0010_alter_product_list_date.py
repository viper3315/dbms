# Generated by Django 4.0.1 on 2022-01-18 15:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_alter_product_list_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='list_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 1, 18, 21, 3, 46, 871403)),
        ),
    ]