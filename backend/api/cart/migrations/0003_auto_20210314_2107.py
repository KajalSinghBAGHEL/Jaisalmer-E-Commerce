# Generated by Django 3.1.7 on 2021-03-14 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0002_auto_20210314_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productrating',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productrating', to='cart.product'),
        ),
    ]
