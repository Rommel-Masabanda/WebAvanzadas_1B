# Generated by Django 4.2.6 on 2024-01-07 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store_app', '0002_producto_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='categoria',
            field=models.CharField(default='Sin categoria', max_length=100),
        ),
    ]
