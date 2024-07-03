# Generated by Django 5.0.2 on 2024-07-03 12:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("monetary", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Transfers",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "in_account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="incoming_transfers",
                        to="monetary.accounts",
                    ),
                ),
                (
                    "out_account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="outgoing_transfers",
                        to="monetary.accounts",
                    ),
                ),
            ],
            options={
                "db_table": "monetary_transfers",
                "ordering": ("out_account", "in_account"),
            },
        ),
    ]
