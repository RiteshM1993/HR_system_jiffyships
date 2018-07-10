# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-09 08:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hrms_employee', '0004_remove_employee_experience_created_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='modified_by',
            new_name='updated_by',
        ),
        migrations.RemoveField(
            model_name='employee',
            name='modified_date',
        ),
        migrations.RemoveField(
            model_name='employee_doc',
            name='modified_date',
        ),
        migrations.AddField(
            model_name='employee',
            name='updated_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee_dependents',
            name='updated_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee_dependents',
            name='updated_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee_designationpackagehistory',
            name='updated_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee_designationpackagehistory',
            name='updated_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee_doc',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee_doc',
            name='created_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee_doc',
            name='updated_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee_doc',
            name='updated_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee_education',
            name='updated_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee_education',
            name='updated_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee_experience',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee_experience',
            name='updated_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee_experience',
            name='updated_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee_project',
            name='updated_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee_project',
            name='updated_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee_type',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee_type',
            name='created_date',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='employee_type',
            name='updated_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='employee_type',
            name='updated_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='created_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='employee_dependents',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee_dependents',
            name='created_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='employee_designationpackagehistory',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee_designationpackagehistory',
            name='created_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='employee_education',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee_education',
            name='created_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='employee_experience',
            name='created_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='employee_project',
            name='created_by',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee_project',
            name='created_date',
            field=models.DateField(null=True),
        ),
    ]
