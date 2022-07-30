from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Setting",
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
                ("name", models.CharField()),
                ("value", models.CharField()),
                ("is_default", models.BooleanField(db_default=models.Value(True))),
            ],
            options={
                "ordering": ["pk"],
            },
        ),
    ]
