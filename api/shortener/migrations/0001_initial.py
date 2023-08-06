# Generated by Django 4.2.4 on 2023-08-06 11:26

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="URL",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("original_url", models.CharField(max_length=2000)),
                ("short_url", models.CharField(max_length=30)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
            ],
            options={
                "verbose_name": "URL",
                "verbose_name_plural": "URLs",
            },
        ),
    ]
