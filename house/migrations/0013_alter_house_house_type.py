# Generated by Django 4.1 on 2023-01-06 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("house", "0012_alter_house_city"),
    ]

    operations = [
        migrations.AlterField(
            model_name="house",
            name="house_type",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="houses",
                to="house.housetype",
                verbose_name="House type",
            ),
        ),
    ]
