# Generated by Django 5.1.3 on 2024-11-24 00:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_product_tags_product_vendor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category', to='core.category'),
        ),
    ]
