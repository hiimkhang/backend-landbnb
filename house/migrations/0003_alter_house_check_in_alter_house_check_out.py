# Generated by Django 4.1 on 2022-12-19 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("house", "0002_amenity_facility_roomtype_remove_house_street_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="house",
            name="check_in",
            field=models.TimeField(null=True),
        ),
        migrations.AlterField(
            model_name="house",
            name="check_out",
            field=models.TimeField(null=True),
        ),
    ]
