# Generated by Django 5.0.2 on 2024-04-28 23:34

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_propietario_whatsapp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id_cliente', models.AutoField(primary_key=True, serialize=False)),
                ('whatsapp', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=65)),
                ('proveedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
