# Generated by Django 4.2 on 2023-05-17 09:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resources", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="topic",
            name="is_generated",
            field=models.BooleanField(default=False),
        ),
    ]