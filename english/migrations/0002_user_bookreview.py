# Generated by Django 4.2.4 on 2023-08-18 11:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("english", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("user_id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=40)),
                ("password", models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name="bookReview",
            fields=[
                ("review_id", models.AutoField(primary_key=True, serialize=False)),
                ("review", models.TextField()),
                ("rating", models.IntegerField()),
                (
                    "book_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="english.book"
                    ),
                ),
                (
                    "reviewer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="english.user"
                    ),
                ),
            ],
        ),
    ]
