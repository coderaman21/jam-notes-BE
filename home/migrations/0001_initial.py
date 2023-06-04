# Generated by Django 4.2.1 on 2023-05-18 03:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Note",
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
                ("title", models.CharField(blank=True, max_length=500)),
                ("text", models.TextField(blank=True)),
                ("theme", models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
