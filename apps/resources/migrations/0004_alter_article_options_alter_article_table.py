# Generated by Django 4.2 on 2023-05-17 16:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("resources", "0003_article_persona"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="article",
            options={"default_related_name": "articles"},
        ),
        migrations.AlterModelTable(
            name="article",
            table=None,
        ),
    ]
