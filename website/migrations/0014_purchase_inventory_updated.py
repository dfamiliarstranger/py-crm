# Generated by Django 4.1 on 2024-02-07 03:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0013_remove_sales_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='inventory_updated',
            field=models.BooleanField(default=False),
        ),
    ]
