# Generated by Django 5.0.2 on 2024-03-17 03:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('monetary', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'categories',
                'ordering': ['description'],
            },
        ),
        migrations.CreateModel(
            name='Companies',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'companies',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'transactions_payments',
                'ordering': ['date', 'registry'],
            },
        ),
        migrations.CreateModel(
            name='Methods',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='monetary.accounts')),
                ('payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.payments')),
            ],
            options={
                'db_table': 'transactions_methods',
                'ordering': ['payment'],
            },
        ),
        migrations.CreateModel(
            name='Registries',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('favored', models.CharField(max_length=20)),
                ('value', models.DecimalField(decimal_places=2, max_digits=10)),
                ('ordering', models.IntegerField(default=0)),
                ('obs', models.TextField(max_length=120)),
                ('category_n1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_n1', to='transactions.categories')),
                ('category_n2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_n2', to='transactions.categories')),
                ('category_n3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_n3', to='transactions.categories')),
                ('companies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.companies')),
            ],
            options={
                'db_table': 'transactions_registries',
                'ordering': ['date', 'ordering'],
            },
        ),
        migrations.AddField(
            model_name='payments',
            name='registry',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.registries'),
        ),
        migrations.CreateModel(
            name='RegistryItens',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=30)),
                ('amount', models.DecimalField(decimal_places=3, max_digits=8)),
                ('unitary', models.DecimalField(decimal_places=2, max_digits=10)),
                ('registries', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transactions.registries')),
            ],
            options={
                'db_table': 'transactions_itens',
                'ordering': ['description'],
            },
        ),
    ]
