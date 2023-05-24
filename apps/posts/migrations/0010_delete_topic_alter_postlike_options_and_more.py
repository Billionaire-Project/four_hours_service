# Generated by Django 4.2 on 2023-05-17 09:26

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0009_alter_postreceipt_is_postable"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Topic",
        ),
        migrations.AlterModelOptions(
            name="postlike",
            options={"default_related_name": "post_likes"},
        ),
        migrations.AlterModelOptions(
            name="postreport",
            options={"default_related_name": "post_reports"},
        ),
    ]