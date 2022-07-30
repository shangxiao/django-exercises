from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Activity",
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
                ("who", models.CharField(max_length=255)),
                ("when", models.DateTimeField()),
                ("what", models.CharField(max_length=255)),
            ],
        ),
    ]
