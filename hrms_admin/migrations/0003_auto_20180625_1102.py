# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-06-25 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms_admin', '0002_project_master_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_table',
            name='active',
            field=models.CharField(max_length=2000),
        ),
    ]
