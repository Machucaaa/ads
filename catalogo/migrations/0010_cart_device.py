# Generated by Django 5.0.2 on 2024-04-30 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0009_rename_producto_cart_id_producto'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='device',
            field=models.CharField(blank=True, max_length=40, null=True),
        ),
    ]
