# Generated by Django 4.2 on 2023-05-02 20:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0003_braiilepicture_braille_alter_braiilepicture_image"),
    ]

    operations = [
        migrations.CreateModel(
            name="KoreanPicture",
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
                (
                    "image",
                    models.ImageField(
                        default="media/default_img.jpeg", null=True, upload_to=""
                    ),
                ),
                ("korean", models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
