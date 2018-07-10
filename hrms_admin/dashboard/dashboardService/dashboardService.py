from hrms_employee.models import employee
from hrms_admin.models import projecttypemaster
from hrms_admin.models import office_location
from hrms_admin.models import designationmaster
from hrms_admin.models import project_master
from hrms_admin.models import purchase_order
from decimal import *
from datetime import datetime
from datetime import timedelta



class getcount:
    @classmethod
    def getcountdata(cls):
        try:
            empcountqry = employee.objects.count()
            projectcountqry = project_master.objects.count()
            ofcloccountqry = office_location.objects.count()
            designationcountqry = designationmaster.objects.count()
            projMangercountqry = project_master.objects.raw("select 1 project_id, count(distinct(manager_id)) from project_master")
            experingpo = purchase_order.objects.raw("SELECT * FROM purchase_order WHERE po_end_date BETWEEN now() and now() + '1 months'")
            exp_count = len(list(experingpo))
            empresignqry = employee.objects.raw("select 1 emp_id, count(resignation_date) from employee")
            # experingpo = purchase_order.objects.filter(po_end_date=(datetime.now() and datetime.now() + timedelta(days=30)))

            data = {
                'empCount': empcountqry,
                'projectCount': projectcountqry,
                'ofclocationCount': ofcloccountqry,
                'designationCount': designationcountqry,
                'projMangercount': projMangercountqry[0].count,
                'experingpo': exp_count,
                'empresign': empresignqry[0].count,
            }

            return data

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def getmanagerprojectcountdata(cls,id):
        try:
            projMangercountqry = project_master.objects.raw('select 1 project_id,count(*) from project_master where manager_id='+id)
            pocountqry = purchase_order.objects.raw(
                'select 1 po_id,count(*) as count from project_master pm inner join purchase_order po on pm.project_id=po.project_id where pm.manager_id=' + id)
            managerexpiringpocount = purchase_order.objects.raw(
                "select 1 po_id,count(*) as count from project_master pm inner join purchase_order po on pm.project_id=po.project_id where po.po_end_date BETWEEN now() and  now() + '1 months' and pm.manager_id=" + id)
            data = {
                'project_count': projMangercountqry[0].count,
                'po_count': pocountqry[0].count,
                'managerexppo_count': managerexpiringpocount[0].count,
            }

            return data

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj


    @classmethod
    def getProjectManagerEmpAssigned(cls, id):
        try:
            listqry = project_master.objects.raw(
                'select a.project_id,a.project_name,a.start_date,a.end_date,a.resource_count,a.businessunit_id,b.project_type_name,b.proj_typemaster_id,c.bu_name,d.first_name,d.middle_name,d.last_name from project_master a inner join project_type_master b on a.proj_typemaster_id = b.proj_typemaster_id inner join business_unit_master c on a.businessunit_id = c.bu_id inner join employee d on a.manager_id = d.emp_id where a.manager_id='+id)
            projectmasterList = []
            for values in listqry:
                projectmasterList.append({
                    'project_id': values.project_id,
                    'project_name': values.project_name,
                    'proj_typemaster_id': values.project_type_name,
                    'start_date': values.start_date,
                    'end_date': values.end_date,
                    'resource_count': values.resource_count,
                    'businessunit_id': values.bu_name,
                    'emp_id': values.manager_id,
                    'manager_name': ' '.join(filter(None, (values.first_name, values.middle_name, values.last_name))),


                })
            return projectmasterList

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj


    @classmethod
    def get_expiringpolist(cls):
        try:
            listqry = purchase_order.objects.raw("select a.po_amount,a.po_id,a.project_id,a.po_number,a.po_start_date,a.po_end_date,b.customer_id,b.project_name,c.customer_name,d.currency_name, d.currency_logo from purchase_order a inner join project_master b on a.project_id = b.project_id inner join customer_table c on b.customer_id = c.customer_id  inner join currency_master d on d.currency_id=a.po_currency_id WHERE a.po_end_date BETWEEN now() and  now() + '1 months'")
            datalist = []
            for values in listqry:
                # cost = 0.0
                # if values.po_project_cost is not None:
                #     cost = Decimal(values.po_project_cost)
                datalist.append({
                    'po_amount':values.currency_logo+' '+ values.po_amount,
                    # 'po_project_cost': cost,
                    # 'po_billing_per_hour': values.po_billing_per_hour,
                    'po_id': values.po_id,
                    'po_number': values.po_number,
                    'po_start_date': values.po_start_date,
                    'po_end_date': values.po_end_date,
                    # 'po_resource_count': values.po_resource_count,
                    'project_name':  values.project_name + " (" + (values.customer_name) + ")",
                    # 'project_type_name': values.project_type_name,
                    'currency_name': values.currency_name,
                })

            return datalist


        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def getmanagerpodata(cls,id):
        try:
            listqry = purchase_order.objects.raw(
                "select a.po_amount,a.po_id,a.project_id,a.po_number, b.customer_id ,b.project_name,c.customer_name,d.currency_name,d.currency_logo from purchase_order a inner join project_master b on a.project_id = b.project_id inner join customer_table c on b.customer_id = c.customer_id  inner join currency_master d on d.currency_id = a.po_currency_id WHERE b.manager_id="+id)
            datalist = []
            for values in listqry:
                datalist.append({
                    'po_amount': values.currency_logo + ' ' + values.po_amount,
                    'po_id': values.po_id,
                    'po_number': values.po_number,
                    'po_start_date': values.po_start_date,
                    'po_end_date': values.po_end_date,
                    'project_name': values.project_name,
                    'currency_name': values.currency_name,
                    'customer_id': values.project_name + " (" + (values.customer_name) + ")",
                })

            return datalist

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def getmanagerexpoodata(cls, id):
        try:
            listqry = purchase_order.objects.raw(
                "select a.po_amount,a.po_id,a.project_id,a.po_number,a.po_start_date,a.po_end_date,b.customer_id,b.project_name,c.customer_name,d.currency_name, d.currency_logo from purchase_order a inner join project_master b on a.project_id = b.project_id inner join customer_table c on b.customer_id = c.customer_id  inner join currency_master d on d.currency_id=a.po_currency_id WHERE a.po_end_date BETWEEN now() and  now() + '1 months' and b.manager_id=" + id)
            datalist = []
            for values in listqry:
                datalist.append({
                    'po_amount': values.currency_logo + ' ' + values.po_amount,
                    # 'po_project_cost': cost,
                    # 'po_billing_per_hour': values.po_billing_per_hour,
                    'po_id': values.po_id,
                    'po_number': values.po_number,
                    'po_start_date': values.po_start_date,
                    'po_end_date': values.po_end_date,
                    # 'po_resource_count': values.po_resource_count,
                    'project_name': values.project_name + " (" + (values.customer_name) + ")",
                    # 'project_type_name': values.project_type_name,
                    'currency_name': values.currency_name,
                })

            return datalist

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def getemployeeresignations(cls, id):
        try:
            listqry = purchase_order.objects.raw(
                "Select emp_id,date_of_leaving,resignation_date,reason_of_leaving,first_name, middle_name, last_name from employee where date_of_leaving is not null")
            datalist = []
            for values in listqry:
                datalist.append({
                    'dol': values.date_of_leaving,
                    'resignReason': values.reason_of_leaving,
                    'resignDate': values.resignation_date,
                    # 'emp_id': values.upload_doc_name,
                    'emp_name': ' '.join(filter(None, (values.first_name, values.middle_name, values.last_name))),
                })


            return datalist

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def listEmployeeresignations(cls, id):
        try:
            listqry = employee.objects.raw(
                "Select emp_id,date_of_leaving,resignation_date,reason_of_leaving,first_name, middle_name, last_name from employee where manager_id="+id)
            datalist = []
            for values in listqry:
                datalist.append({
                    'dol': values.date_of_leaving,
                    'resignReason': values.reason_of_leaving,
                    'resignDate': values.resignation_date,
                    # 'emp_id': values.upload_doc_name,
                    'emp_name': ' '.join(filter(None, (values.first_name, values.middle_name, values.last_name))),
                })

            return datalist

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj