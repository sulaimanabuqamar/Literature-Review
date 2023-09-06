# Generated by Django 4.2.4 on 2023-09-04 15:10

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("english", "0004_alter_bookreview_reviewer_delete_user"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="bookReview",
            new_name="Review",
        ),
        migrations.RenameField(
            model_name="review",
            old_name="book_id",
            new_name="passage_id",
        ),
    ]
