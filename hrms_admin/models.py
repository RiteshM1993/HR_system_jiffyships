# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from decimal import Decimal

from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


class businessunitmaster(models.Model):
    bu_id = models.AutoField(primary_key=True)
    bu_name = models.CharField(max_length=4000)
    bu_parentid = models.IntegerField(null=True)
    active = models.BooleanField(default=False)
    bu_manager_id = models.IntegerField(null=True)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)

    class Meta:
        db_table = "business_unit_master"


class currencymaster(models.Model):
    currency_id = models.AutoField(primary_key=True)
    currency_name = models.CharField(max_length=2000)
    currency_logo = models.CharField(max_length=1000)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)

    class Meta:
        db_table = "currency_master"


class designationmaster(models.Model):
    designation_id = models.AutoField(primary_key=True)
    designation_name = models.CharField(max_length=2500)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)

    class Meta:
        db_table = "designation_master"


class projecttypemaster(models.Model):
    proj_typemaster_id = models.AutoField(primary_key=True)
    project_type_name = models.CharField(max_length=3000)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)

    class Meta:
        db_table = "project_type_master"

class office_location(models.Model):
    location_id = models.AutoField(primary_key=True)
    office_location = models.CharField(max_length=2000)
    address = models.CharField(max_length=4000)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)

    class Meta:
        db_table = "office_location"


class project_master(models.Model):
    project_id=models.AutoField(primary_key=True)
    project_name=models.CharField(max_length=2000)
    proj_typemaster_id=models.BigIntegerField()
    start_date = models.DateField()
    end_date = models.DateField(null=True)
    resource_count=models.BigIntegerField()
    businessunit_id=models.BigIntegerField()
    manager_id=models.BigIntegerField(null=True)
    customer_id = models.BigIntegerField(null=True)
    project_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)



    class Meta:
        db_table="project_master"


class project_documents(models.Model):
    proj_doc_id=models.AutoField(primary_key=True)
    project_id=models.BigIntegerField()
    doc_name=models.CharField(max_length=2000)
    doc_file = models.CharField(max_length=2000, null=True)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)

    class Meta:
        db_table="project_documents"



class billing(models.Model):
    bill_id=models.AutoField(primary_key=True)
    project_id=models.BigIntegerField()
    billable_resource_count=models.DecimalField(max_digits=20,decimal_places=2)
    total_bill=models.DecimalField(max_digits=20,decimal_places=2)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)


    class Meta:
        db_table="billing"


class customer_table(models.Model):
    customer_id=models.AutoField(primary_key=True)
    customer_name=models.CharField(max_length=2000)
    customer_address=models.CharField(max_length=2000)
    start_date = models.DateField()
    contact_person_name=models.CharField(max_length=2000)
    contact_person_emailid=models.CharField(max_length=4000)
    active = models.CharField(max_length=2000,null=True)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)


    class Meta:
        db_table = "customer_table"


class purchase_order(models.Model):
    po_id = models.AutoField(primary_key=True)
    project_id = models.BigIntegerField()
    po_number = models.BigIntegerField()
    po_start_date = models.DateField(null=True)
    po_end_date = models.DateField(null=True)
    # po_resource_count = models.BigIntegerField()
    # po_billing_type = models.BigIntegerField()
    po_amount = models.CharField(max_length=2000)
    # po_billing_per_hour = models.BigIntegerField(null=True)
    # po_project_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    po_currency_id = models.BigIntegerField()
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)


    class Meta:
        db_table = "purchase_order"













