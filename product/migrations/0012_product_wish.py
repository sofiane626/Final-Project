# Generated by Django 4.2.2 on 2023-07-18 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_rename_taillel_product_stock_remove_product_taillem_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='wish',
            field=models.BooleanField(default=False),
        ),
    ]
