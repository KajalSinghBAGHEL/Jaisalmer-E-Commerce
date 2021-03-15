# Generated by Django 3.1.7 on 2021-03-14 16:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cart", "0005_auto_20210314_2126"),
    ]

    operations = [
        migrations.AlterField(
            model_name="productrating",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="user_id",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
