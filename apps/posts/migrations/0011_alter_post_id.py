# Generated by Django 4.2 on 2023-05-17 09:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0010_delete_topic_alter_postlike_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="id",
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
