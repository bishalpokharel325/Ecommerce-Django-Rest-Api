# Generated by Django 3.1.7 on 2021-02-27 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210227_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cash_on_delivery',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='discount_expiry',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='discount_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='free_shipping',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='warranty_years',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=20),
        ),
    ]
