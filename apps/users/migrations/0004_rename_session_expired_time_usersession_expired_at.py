# Generated by Django 4.2 on 2023-04-28 17:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0003_rename_logged_in_at_usersession_issued_at_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usersession",
            old_name="session_expired_time",
            new_name="expired_at",
        ),
    ]
