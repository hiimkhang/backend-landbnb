# Generated by Django 4.1 on 2023-01-06 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reservation", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BookedDay",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_on", models.DateTimeField(auto_now_add=True)),
                ("updated_on", models.DateField(auto_now=True)),
                ("day", models.DateField()),
                (
                    "reservation",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="reservation.reservation",
                    ),
                ),
            ],
            options={
                "verbose_name": "Booked Day",
                "verbose_name_plural": "Booked Days",
            },
        ),
    ]