# Generated by Django 4.2 on 2023-04-28 18:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0005_alter_usersession_issued_at"),
    ]

    operations = [
        migrations.AddField(
            model_name="usersession",
            name="auth_time",
            field=models.DateTimeField(default=None, null=True),
        ),
    ]