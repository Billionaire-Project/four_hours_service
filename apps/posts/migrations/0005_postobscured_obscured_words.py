# Generated by Django 4.2 on 2023-05-05 03:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0004_postobscured_is_failed_postobscured_time_taken_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="postobscured",
            name="obscured_words",
            field=models.TextField(default=""),
        ),
    ]
