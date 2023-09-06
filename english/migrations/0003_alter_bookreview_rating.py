# Generated by Django 4.2.4 on 2023-08-18 11:24

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("english", "0002_user_bookreview"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookreview",
            name="rating",
            field=models.PositiveIntegerField(
                choices=[
                    (1, "1 star"),
                    (2, "2 stars"),
                    (3, "3 stars"),
                    (4, "4 stars"),
                    (5, "5 stars"),
                ]
            ),
        ),
    ]
