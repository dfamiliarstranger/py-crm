# Generated by Django 4.1 on 2023-11-28 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_purchase_size_sales_size'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='size',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
    ]
