# Generated by Django 4.2 on 2023-05-31 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("resources", "0019_postgenerated_is_posted"),
        ("posts", "0012_post_is_generated"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="generated_post",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="resources.postgenerated",
            ),
        ),
    ]
