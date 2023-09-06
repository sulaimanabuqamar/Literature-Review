# Generated by Django 4.2.4 on 2023-09-04 15:17

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("english", "0005_rename_bookreview_review_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Review",
            new_name="bookReview",
        ),
        migrations.RenameField(
            model_name="bookreview",
            old_name="passage_id",
            new_name="book_id",
        ),
    ]
