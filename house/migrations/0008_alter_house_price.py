# Generated by Django 4.1 on 2023-01-05 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("house", "0007_remove_photo_room_photo_house_alter_photo_file"),
    ]

    operations = [
        migrations.AlterField(
            model_name="house",
            name="price",
            field=models.IntegerField(default=0),
        ),
    ]
