# Generated by Django 4.2 on 2023-05-24 14:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("resources", "0014_rename_is_used_article_is_summary_articlesummary"),
    ]

    operations = [
        migrations.AddField(
            model_name="articlesummary",
            name="is_failed",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="articlesummary",
            name="time_taken",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="articlesummary",
            name="total_token",
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
