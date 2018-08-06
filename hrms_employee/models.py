# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
# models.ForeignKey(designationmaster, on_delete=models.CASCADE)
class hremployee(models.Model):
    emp_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=4000, null=True)
    middle_name = models.CharField(max_length=4000, null=True)
    last_name = models.CharField(max_length=4000, null=True)
    employee_no = models.CharField(max_length=4000, null=True)
    email_id = models.CharField(max_length=4000)
    mobile_number = models.CharField(max_length=4000, null=True)
    year_exp = models.IntegerField(null=True)
    address = models.CharField(max_length=4000, null=True)
    permanent_address = models.CharField(max_length=4000, null=True)
    emp_image = models.CharField(max_length=4000, null=True)
    emp_role = models.CharField(max_length=4000, null=True)
    created_by = models.IntegerField(null=True)
    updated_by = models.IntegerField(null=True)
    created_date = models.DateField(null=True)
    updated_date = models.DateField(null=True)

    class Meta:
        db_table = "hremployee"

#
# class employee_doc(models.Model):
#     docId = models.AutoField(primary_key=True)
#     emp_id = models.BigIntegerField()
#     doc_name = models.CharField(max_length=2000)
#     upload_doc_name = models.CharField(max_length=2000, null=True)
#     created_by = models.IntegerField(null=True)
#     updated_by = models.IntegerField(null=True)
#     created_date = models.DateField(null=True)
#     updated_date = models.DateField(null=True)
#
#     class Meta:
#         db_table = "employee_doc"


