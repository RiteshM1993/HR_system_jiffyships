from hrms_admin.models import project_master
from hrms_admin.businessunitmaster.businessUnitMasterService.businessUnitMasterService import businessUnitMaster
# from hrms_admin.designationmaster.designationmasterservice.designationmasterservice import dmdesignation
from hrms_admin.projecttypemaster.projecttypemasterservice.projecttypemasterservice import dmprojecttype
# from hrms_admin.models import designationmaster
from  hrms_employee.models import employee
from  hrms_admin.models import customer_table
from hrms_admin.customermaster.customermasterservice.customermasterservice import dmcustomermaster
from decimal import *


class dmprojectmaster:
    @classmethod
    def saveProjectMaster(self, projectName,projecttypeMasterid,startDate,endDate,resourceCount,businessUNitid,emp_id,customerId,projectCost,created_by,created_date):
        try:
            saveqry = project_master(project_name=projectName,proj_typemaster_id=projecttypeMasterid,start_date =startDate,end_date=endDate,resource_count =resourceCount,businessunit_id=businessUNitid,created_by=created_by,created_date=created_date,manager_id=emp_id,customer_id=customerId,project_cost=projectCost)

            saveqry.save()

            saveqrysuccessobj = {
                'response': "success"
            }
            return saveqrysuccessobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return {'failureobj': saveqryfailureobj}

    @classmethod
    def listemployeevalues(cls, name):
        try:
            name_str = name
            employeeList = []
            if ' ' in name_str:
                name_str = name_str.replace(' ', '%%')
                listqry = employee.objects.raw(
                    "Select emp_id, email_id,CONCAT(first_name,' ',middle_name,' ',last_name) as employee_name from employee where lower( CONCAT(first_name,' ',middle_name,' ',last_name)) like '%%" + name_str + "%%'")

            else:
                listqry = employee.objects.raw(
                    "Select emp_id, email_id,CONCAT(first_name,' ',middle_name,' ',last_name) as employee_name from employee where lower( CONCAT(first_name,' ',middle_name,' ',last_name)) like  '%%" + name_str + "%%'")

            for values in listqry:
                employeeList.append({
                    "emp_name": values.employee_name,
                    # "emp_id": values.emp_id,
                    "email_id": values.email_id,
                    "emp_id": values.emp_id,

                })

            return employeeList

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def listprojectMaster(self):
        try:
            listqry = project_master.objects.raw('select a.project_id,a.project_name,a.start_date,a.end_date,a.resource_count,a.customer_id,a.businessunit_id,b.project_type_name,b.proj_typemaster_id,c.bu_name,d.first_name,d.middle_name,d.last_name,e.customer_id,e.customer_name from project_master a inner join project_type_master b on a.proj_typemaster_id = b.proj_typemaster_id inner join business_unit_master c on a.businessunit_id = c.bu_id inner join employee d on a.manager_id = d.emp_id inner join customer_table e on a.customer_id=e.customer_id')
            projectmasterList = []

            for values in listqry:
                projectmasterList.append({
                    'customer_id':values.project_name + " (" + (values.customer_name)+")",
                    'customerID':values.customer_id,
                    'customer_name':values.customer_name,
                    'project_id': values.project_id,
                    'project_name': values.project_name,
                    'proj_typemaster_id': values.project_type_name,
                    'start_date': values.start_date,
                    'end_date': values.end_date,
                    'resource_count': values.resource_count,
                    'businessunit_id': values.bu_name,
                    'emp_id': values.manager_id,
                    'project_cost':values.project_cost,
                    'manager_name': ' '.join(filter(None, (values.first_name, values.middle_name, values.last_name))),
                    # 'project_doc_name' : values.doc_name,
                    # 'project_doc_file_name': values.doc_file,
                    # 'curr_rate':currency_name + " " + rate_per_hour,
                    # 'curr_rate':' '.join(None[values.currency_name, values.rate_per_hour]),

                })
            return projectmasterList

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj




    @classmethod
    def deleteprojectmaster(self, id):
        try:
            delqry = project_master.objects.get(project_id=id)

            delqry.delete()
            saveqrysuccessobj = {
                'response': "success"
            }
            return saveqrysuccessobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj


    @classmethod
    def getprojectmasterdata(self,id):
        try:

            # getqry = employee_project.objects.get(emp_proj_id=id)
            getqry = project_master.objects.raw('select a.project_id,a.project_name,a.start_date,a.end_date,a.resource_count,a.businessunit_id,a.customer_id,b.project_type_name,b.proj_typemaster_id,c.bu_name,c.bu_id,d.first_name,d.middle_name,d.last_name,e.customer_id from project_master a inner join project_type_master b on a.proj_typemaster_id = b.proj_typemaster_id inner join business_unit_master c on a.businessunit_id = c.bu_id inner join employee d on a.manager_id = d.emp_id inner join customer_table e on a.customer_id=e.customer_id where a.project_id='+id)
            for data in getqry:
                dataobj = {
                    'customer_id': data.customer_id,
                    'project_id': data.project_id,
                    'project_name': data.project_name,
                    'proj_typemaster_id': data.proj_typemaster_id,
                    'proj_typemaster_name':data.project_type_name,
                    'start_date':data.start_date,
                    'end_date': data.end_date,
                    'resource_count': data.resource_count,
                    'businessunit_id': data.bu_id,
                    'businessunit_name': data.bu_name,
                    'emp_id': data.manager_id,
                    'project_cost': int(data.project_cost),
                    'manager_name': ' '.join(filter(None, (data.first_name, data.middle_name, data.last_name))),

                }

            return dataobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def updateeprojectmaster(self, id,projectName ,projecttypeMasterid,start_date,end_date,resourceCount,businessUNitid,emp_id,customer_id,projectCost,updated_by, updated_date):
        try:
            getqry = project_master.objects.get(project_id=id)
            getqry.customer_id = customer_id
            getqry.project_name = projectName
            getqry.proj_typemaster_id  = projecttypeMasterid
            getqry.start_date = start_date
            getqry.end_date = end_date
            getqry.resource_count=resourceCount
            getqry.updated_date = updated_date
            getqry.updated_by = updated_by
            getqry.businessunit_id=businessUNitid
            getqry.manager_id=emp_id
            # getqry.currency_name=currency_name
            # getqry.rate_per_hour=rate_per_hour
            getqry.project_cost=projectCost


            getqry.save()

            saveqrysuccessobj = {
                'response': "success"
            }
            return saveqrysuccessobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return {'failureobj': saveqryfailureobj}

    # @classmethod
    # def employeebusinessunitvalues(cls):
    #     dm_customermaster = dmcustomermaster()
    #     list_customer = dm_customermaster.listcustomer()
    #     return list_customer

    @classmethod
    def getcustomervalues(cls):
        dm_customermaster = dmcustomermaster()
        list_customer = dm_customermaster.listcustomer()
        return list_customer

    @classmethod
    def employeebusinessunitvalues(cls):
        business_unit_master_object = businessUnitMaster()
        business_unit = business_unit_master_object.listBusinessUnitMaster()
        return business_unit

    @classmethod
    def projecttypevalues(cls):
        dm_projecttype = dmprojecttype.listProjecttype()
        return dm_projecttype


    @classmethod
    def getProjectDocument(cls, id):
        try:
            listqry = project_master.objects.raw(
                'select a.project_id, b.project_name,a.doc_file,a.doc_name from project_documents a inner join project_master b on a.project_id= b.project_id where a.project_id=' + id)

            projectDocList = []

            for values in listqry:
                projectDocList.append({
                    'project_id': values.project_id,
                    'project_name': values.project_name,
                    'doc_file': values.doc_file,
                    'doc_name': values.doc_name,
                })
            return projectDocList

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def getprojectpo(cls, id):
        try:
            listqry = project_master.objects.raw('select a.po_amount,a.po_id,a.project_id,a.po_number,a.po_start_date,a.po_end_date,b.project_name,b.customer_id,c.customer_name,d.currency_name,d.currency_logo from purchase_order a inner join project_master b on a.project_id = b.project_id inner join customer_table c on b.customer_id=c.customer_id inner join currency_master d on d.currency_id=a.po_currency_id where a.project_id='+id)


            datalist = []
            for values in listqry:
                # cost = 0.0
                # if values.po_project_cost is not None:
                #     cost = Decimal(values.po_project_cost)
                datalist.append({
                    'po_amount': values.currency_logo+' '+ values.po_amount,
                    # 'po_project_cost': cost,
                    # 'po_billing_per_hour': values.po_billing_per_hour,
                    'po_id': values.po_id,
                    'po_number': values.po_number,
                    'po_start_date': values.po_start_date,
                    'po_end_date': values.po_end_date,
                    # 'po_resource_count': values.po_resource_count,
                    'project_name':values.project_name + " (" + (values.customer_name)+")",
                    'customer_name':values.customer_name,
                    # 'project_type_name': values.project_type_name,
                    'currency_name': values.currency_name,
                })
            return datalist

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def getcustomerproject(cls, id):
        try:
            listqry = customer_table.objects.raw(
                'select a.manager_id,a.project_id,a.project_name,a.start_date,a.end_date,a.resource_count,a.customer_id,a.businessunit_id,b.project_type_name,b.proj_typemaster_id,c.bu_name,d.first_name,d.middle_name,d.last_name,e.customer_name from project_master a inner join project_type_master b on a.proj_typemaster_id = b.proj_typemaster_id inner join business_unit_master c on a.businessunit_id = c.bu_id inner join employee d on a.manager_id = d.emp_id inner join customer_table e on a.customer_id=e.customer_id where a.customer_id=' + id)

            projectmasterList = []

            for values in listqry:
                projectmasterList.append({
                    'customer_id': values.customer_name,
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
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj


