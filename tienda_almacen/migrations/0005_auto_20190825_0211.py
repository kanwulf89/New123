# Generated by Django 2.2.3 on 2019-08-25 02:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_almacen', '0004_auto_20190825_0210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='categoria_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='tienda_almacen.Categoria'),
        ),
    ]
