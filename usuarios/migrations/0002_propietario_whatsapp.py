# Generated by Django 5.0.2 on 2024-04-25 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='propietario',
            name='whatsapp',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
