# Generated by Django 4.1 on 2023-11-12 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_purchase_total_alter_purchase_product_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='color',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='product_type',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='unit',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='unit_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10),
        ),
    ]