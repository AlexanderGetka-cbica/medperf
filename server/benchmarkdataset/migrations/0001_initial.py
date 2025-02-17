# Generated by Django 3.2.10 on 2022-03-07 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("benchmark", "__first__"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("dataset", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="BenchmarkDataset",
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
                    "approval_status",
                    models.CharField(
                        choices=[
                            ("PENDING", "PENDING"),
                            ("APPROVED", "APPROVED"),
                            ("REJECTED", "REJECTED"),
                        ],
                        default="PENDING",
                        max_length=100,
                    ),
                ),
                ("approved_at", models.DateTimeField(blank=True, null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                (
                    "benchmark",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="benchmark.benchmark",
                    ),
                ),
                (
                    "dataset",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="dataset.dataset",
                    ),
                ),
                (
                    "initiated_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={"ordering": ["modified_at"],},
        ),
    ]
