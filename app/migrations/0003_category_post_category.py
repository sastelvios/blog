# Generated by Django 4.1.7 on 2023-02-24 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_post_cover_alter_post_content_alter_post_summary"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category", models.TextField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name="post",
            name="category",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.PROTECT,
                to="app.category",
            ),
            preserve_default=False,
        ),
    ]
