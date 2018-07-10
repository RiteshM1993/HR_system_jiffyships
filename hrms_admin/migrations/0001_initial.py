# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-19 08:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='billing',
            fields=[
                ('bill_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_id', models.BigIntegerField()),
                ('billable_resource_count', models.DecimalField(decimal_places=2, max_digits=20)),
                ('total_bill', models.DecimalField(decimal_places=2, max_digits=20)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('created_by', models.BigIntegerField(null=True)),
                ('created_date', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'billing',
            },
        ),
        migrations.CreateModel(
            name='businessunitmaster',
            fields=[
                ('bu_id', models.AutoField(primary_key=True, serialize=False)),
                ('bu_name', models.CharField(max_length=4000)),
                ('bu_parentid', models.IntegerField(null=True)),
                ('active', models.BooleanField(default=False)),
                ('bu_manager_id', models.IntegerField(null=True)),
            ],
            options={
                'db_table': 'business_unit_master',
            },
        ),
        migrations.CreateModel(
            name='currencymaster',
            fields=[
                ('currency_id', models.AutoField(primary_key=True, serialize=False)),
                ('currency_name', models.CharField(max_length=2000)),
                ('currency_logo', models.CharField(max_length=1000)),
            ],
            options={
                'db_table': 'currency_master',
            },
        ),
        migrations.CreateModel(
            name='customer_table',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_name', models.CharField(max_length=2000)),
                ('customer_address', models.CharField(max_length=2000)),
                ('start_date', models.DateField()),
                ('contact_person_name', models.CharField(max_length=2000)),
                ('contact_person_emailid', models.CharField(max_length=4000)),
                ('created_by', models.BigIntegerField()),
                ('created_date', models.DateTimeField()),
                ('active', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'customer_table',
            },
        ),
        migrations.CreateModel(
            name='designationmaster',
            fields=[
                ('designation_id', models.AutoField(primary_key=True, serialize=False)),
                ('designation_name', models.CharField(max_length=2500)),
            ],
            options={
                'db_table': 'designation_master',
            },
        ),
        migrations.CreateModel(
            name='office_location',
            fields=[
                ('location_id', models.AutoField(primary_key=True, serialize=False)),
                ('office_location', models.CharField(max_length=2000)),
                ('address', models.CharField(max_length=4000)),
                ('created_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'office_location',
            },
        ),
        migrations.CreateModel(
            name='project_documents',
            fields=[
                ('proj_doc_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_id', models.BigIntegerField()),
                ('doc_name', models.CharField(max_length=2000)),
                ('doc_file', models.CharField(max_length=2000, null=True)),
                ('created_by', models.BigIntegerField(null=True)),
                ('created_date', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'project_documents',
            },
        ),
        migrations.CreateModel(
            name='project_master',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_name', models.CharField(max_length=2000)),
                ('proj_typemaster_id', models.BigIntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(null=True)),
                ('resource_count', models.BigIntegerField()),
                ('created_by', models.BigIntegerField()),
                ('created_date', models.DateTimeField()),
                ('modified_date', models.DateTimeField(null=True)),
                ('businessunit_id', models.BigIntegerField()),
                ('manager_id', models.BigIntegerField(null=True)),
            ],
            options={
                'db_table': 'project_master',
            },
        ),
        migrations.CreateModel(
            name='projecttypemaster',
            fields=[
                ('proj_typemaster_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_type_name', models.CharField(max_length=3000)),
            ],
            options={
                'db_table': 'project_type_master',
            },
        ),
        migrations.CreateModel(
            name='purchase_order',
            fields=[
                ('po_id', models.AutoField(primary_key=True, serialize=False)),
                ('project_id', models.BigIntegerField()),
                ('po_number', models.BigIntegerField()),
                ('po_start_date', models.DateField(null=True)),
                ('po_end_date', models.DateField(null=True)),
                ('po_resource_count', models.BigIntegerField()),
                ('po_billing_type', models.BigIntegerField()),
                ('po_amount', models.CharField(max_length=2000)),
                ('po_billing_per_hour', models.BigIntegerField(null=True)),
                ('po_project_cost', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('po_currency_id', models.BigIntegerField()),
                ('created_date', models.DateField(null=True)),
                ('created_by', models.BigIntegerField()),
            ],
            options={
                'db_table': 'purchase_order',
            },
        ),
    ]
