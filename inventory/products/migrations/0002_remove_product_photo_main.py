# Generated by Django 4.0.1 on 2022-01-17 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='photo_main',
        ),
    ]