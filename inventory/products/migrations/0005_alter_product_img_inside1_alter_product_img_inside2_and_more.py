# Generated by Django 4.0.1 on 2022-01-18 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_product_img_inside1_product_img_inside2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img_inside1',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_inside2',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_inside3',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_inside4',
            field=models.ImageField(blank=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='product',
            name='img_inside5',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
