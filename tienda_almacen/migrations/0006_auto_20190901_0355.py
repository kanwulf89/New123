# Generated by Django 2.2.3 on 2019-09-01 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_almacen', '0005_auto_20190825_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='precio_unidad',
            field=models.DecimalField(blank=True, decimal_places=6, default=None, max_digits=19, null=True),
        ),
    ]
