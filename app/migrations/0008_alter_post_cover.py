# Generated by Django 4.1.7 on 2023-02-24 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0007_alter_post_cover"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="cover",
            field=models.ImageField(upload_to=""),
        ),
    ]
