# Generated by Django 4.1 on 2023-11-16 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_inventoryitem_size_alter_inventoryitem_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventoryitem',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
