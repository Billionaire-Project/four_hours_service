# Generated by Django 4.2 on 2023-05-19 06:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resources", "0006_postgenerated_article"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="is_used",
            field=models.BooleanField(default=False),
        ),
    ]