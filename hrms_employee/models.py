# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# models.ForeignKey(designationmaster, on_delete=models.CASCADE)
class employee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    email_id = models.CharField(max_length=4000)
    date_of_joining = models.DateField(null=True)
    date_of_leaving = models.DateField(null=True)
    status_id = models.IntegerField(null=True)
    jobtitle_id = models.IntegerField(null=True)
    mobile_number = models.CharField(max_length=4000, null=True)
    office_number = models.CharField(max_length=4000, null=True)
    isactive = models.IntegerField(null=True)
    year_exp = models.IntegerField(null=True)
    businessunit_id = models.IntegerField(null=True)
    manager_id = models.IntegerField(null=True)
    personal_email = models.CharField(max_length=4000, null=True)
    first_name = models.CharField(max_length=4000, null=True)
    middle_name = models.CharField(max_length=4000, null=True)
    last_name = models.CharField(max_length=4000, null=True)
    birth_date = models.DateField(null=True)
    address = models.CharField(max_length=4000, null=True)
    permanent_address = models.CharField(max_length=4000, null=True)
    office_location_id = models.IntegerField(null=True)
    emp_dm_id = models.CharField(max_length=4000, null=True)
    emp_image = models.CharField(max_length=4000, null=True)
    resignation_date = models.DateTimeField(null=True)
    reason_of_leaving = models.CharField(max_length=8000, null=True)
    emp_role = models.CharField(max_length=4000, null=True)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)
    resign_status = models.IntegerField(null=True)

    class Meta:
        db_table = "employee"


class employee_dependents(models.Model):
    dependent_id = models.AutoField(primary_key=True)
    emp_id  = models.BigIntegerField()
    dependent_name = models.CharField(max_length=4000)
    relation = models.CharField(max_length=4000)
    dob = models.DateField()
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)

    class Meta:
        db_table = "employee_dependents"

class employee_designationpackagehistory(models.Model):
    pckg_id = models.AutoField(primary_key=True)
    emp_id = models.IntegerField()
    salary = models.FloatField()
    from_date = models.DateField()
    active = models.IntegerField()
    currency_id = models.BigIntegerField()
    designation_id = models.BigIntegerField()
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)

    class Meta:
        db_table = "employee_designationpackagehistory"

class employee_education(models.Model):
    emp_edu_id = models.AutoField(primary_key=True)
    emp_id = models.BigIntegerField()
    school_univeristy_name = models.CharField(max_length=3000)
    qualification_degree_name = models.CharField(max_length=1000)
    date_of_completion = models.DateField()
    notes = models.CharField(max_length=1000)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)

    class Meta:
        db_table = "employee_education"

class employee_experience(models.Model):
    emp_expr_id = models.AutoField(primary_key=True)
    emp_id = models.BigIntegerField()
    prev_company_name = models.CharField(max_length=5000)
    job_title = models.CharField(max_length=2500)
    from_date = models.DateField()
    to_date = models.DateField()
    job_description = models.CharField(max_length=5000)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)

    class Meta:
        db_table = "employee_experience"

class employee_project(models.Model):
    emp_proj_id = models.AutoField(primary_key=True)
    emp_id = models.BigIntegerField()
    project_id = models.BigIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    billing_type = models.BigIntegerField(null=True)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)


    class Meta:
        db_table = "employee_project"

class employee_type(models.Model):
    emp_typeId = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=2000)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)

    class Meta:
        db_table = "employee_type"

class employee_doc(models.Model):
    docId = models.AutoField(primary_key=True)
    emp_id = models.BigIntegerField()
    doc_name = models.CharField(max_length=2000)
    upload_doc_name = models.CharField(max_length=2000, null=True)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)

    class Meta:
        db_table = "employee_doc"


