# Generated by Django 5.0.2 on 2024-07-03 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("monetary", "0003_transfers_value"),
    ]

    operations = [
        migrations.AddField(
            model_name="transfers",
            name="date",
            field=models.DateField(),
            preserve_default=False,
        ),
    ]