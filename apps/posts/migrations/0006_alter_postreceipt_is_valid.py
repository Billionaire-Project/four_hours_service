# Generated by Django 4.2 on 2023-05-06 08:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0005_postobscured_obscured_words"),
    ]

    operations = [
        migrations.AlterField(
            model_name="postreceipt",
            name="is_valid",
            field=models.BooleanField(default=False),
        ),
    ]
