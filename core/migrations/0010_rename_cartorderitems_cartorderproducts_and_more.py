# Generated by Django 5.1.3 on 2024-12-02 08:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_product_description_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CartOrderItems',
            new_name='CartOrderProducts',
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, default='This is the product', null=True),
        ),
        migrations.AlterField(
            model_name='productreview',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='reviews', to='core.product'),
        ),
    ]
