from hrms_employee.models import employee_project
from hrms_employee.employee.employeeservice.employeeservice import dmemployee
from hrms_admin.projecttypemaster.projecttypemasterservice.projecttypemasterservice import dmprojecttype
import datetime
from hrms_admin.models import designationmaster
from hrms_admin.models import project_master
from hrms_employee.models import employee


class dmemployeeproject:
    @classmethod
    def saveEmployeeproject(self, emp_id,project_id,start_Date,end_Date,empdesc,created_by,created_date):
        try:
            successobj = {}
            getqry = employee_project.objects.raw('select * from employee_project where emp_id=%s and project_id=%s'%(emp_id,project_id))
            count = 0
            for values in getqry:
                count = count+1
            if count==1:
                successobj = {'data': 'employee already assigned to this project'}
            else:
                saveqry = employee_project(emp_id=emp_id, project_id=project_id, start_date=start_Date,
                                           end_date=end_Date, created_by=created_by, created_date=created_date, billing_type=empdesc)
                saveqry.save()
                successobj = {'data': 'success'}



            return successobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def listemployeevalues(cls, name):
        try:
            name_str = name
            employeeList = []
            if ' ' in name_str:
                name_str = name_str.replace(' ', '%%')
                listqry = employee.objects.raw("Select emp_id, email_id,CONCAT(first_name,' ',middle_name,' ',last_name) as employee_name from employee where lower( CONCAT(first_name,' ',middle_name,' ',last_name)) like '%%" + name_str + "%%'")

            else:
                listqry = employee.objects.raw("Select emp_id, email_id,CONCAT(first_name,' ',middle_name,' ',last_name) as employee_name from employee where lower( CONCAT(first_name,' ',middle_name,' ',last_name)) like  '%%" + name_str + "%%'")

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
    def listEmployeeproject(self):
        try:
            listqry = employee_project.objects.raw('select a.billing_type,a.emp_proj_id,a.start_date,a.end_date,a.project_id,b.first_name,b.middle_name,b.last_name,c.project_name,c.project_id from employee_project a inner join employee b on a.emp_id = b.emp_id inner join project_master c on a.project_id = c.project_id')
            employeeprojectList = []

            for values in listqry:
                employeeprojectList.append({
                    'emp_proj_id':values.emp_proj_id,
                    'emp_id': values.emp_id,
                    'project_name':values.project_name,
                    'emp_name':' '.join(filter(None,(values.first_name,values.middle_name,values.last_name))),
                    'project_id': values.project_id,
                    'start_date': values.start_date,
                    'end_date': values.end_date,
                    'emp_desc': values.billing_type,
                    # 'currency_name':values.currency_name,
                    # 'rate_per_hour':values.rate_per_hour,
                })
            return employeeprojectList

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj


    @classmethod
    def deleteemployeeproject(self,id):
        try:
            delqry = employee_project.objects.get(emp_proj_id =id)

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
    def getEmployeeprojectdata(self,id):
        try:

            getqry = employee_project.objects.raw('select a.billing_type,a.emp_proj_id,a.start_date,a.end_date,a.project_id,b.first_name,b.middle_name,b.last_name,c.project_name,c.project_id from employee_project a inner join employee b on a.emp_id = b.emp_id inner join project_master c on a.project_id = c.project_id where a.emp_proj_id ='+id)
            for data in getqry:
                dataobj = {
                    'emp_proj_id': data.emp_proj_id,
                    'emp_id': data.emp_id,
                    'project_name': data.project_name,
                    'project_id': data.project_id,
                    'emp_name': ' '.join(filter(None,(data.first_name,data.middle_name,data.last_name))),
                    # 'emp_name': getqry.emp_name,
                    # 'project_name': getqry.project_type_name,
                    'start_date':data.start_date,
                    'end_date': data.end_date,
                    'emp_desc' : data.billing_type,
                    # 'currency_name':data.currency_name,
                    # 'rate_per_hour': data.rate_per_hour,

                }

            return dataobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def updateemployeeproject(self,id,emp_id,project_id,start_Date,end_Date,emp_desc,updated_by,updated_date):
        try:
            getqry = employee_project.objects.get(emp_proj_id=id)
            getqry.emp_id=emp_id
            getqry.project_id = project_id
            getqry.start_date = start_Date
            getqry.end_date = end_Date
            getqry.billing_type = emp_desc
            getqry.updated_by = updated_by
            getqry.updated_date = updated_date

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


    @classmethod
    def projectmastertypevalues(cls):
        try:
            listqry=project_master.objects.all()
            projectmasterlist=[]

            for values in listqry:
                projectmasterlist.append({
                    'project_id':values.project_id,
                    'project_name':values.project_name,

                })
            return projectmasterlist

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def getResourceData(cls,id):
        try:
            listqry=employee_project.objects.raw('select b.emp_proj_id,a.project_id, a.project_name, b.emp_id,c.first_name,c.middle_name,c.last_name,c.email_id,c.emp_dm_id,c.emp_image,e.designation_name from project_master a inner join employee_project b on a.project_id = b.project_id inner join employee c on b.emp_id = c.emp_id inner join designation_master e on c.jobtitle_id=e.designation_id where a.project_id='+id)

            projectmasterlist=[]

            for values in listqry:
                projectmasterlist.append({
                    'resourceName': ' '.join(filter(None, (values.first_name , values.middle_name , values.last_name))),
                    'resourceDesignation' : values.designation_name,
                    'dmId': values.emp_dm_id,
                    'dmEmailId': values.email_id,
                    'emp_image' : values.emp_image,


                })
            return projectmasterlist

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def getStartEndDateData(cls, id):
        try:
            listqry = project_master.objects.raw('select project_id,start_date,end_date from project_master where project_id=' + id)

            startEndDate = []

            for values in listqry:
                startEndDate.append({
                    'startDate': values.start_date,
                    'endDate' : values.end_date,

                })
            return startEndDate

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj



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
                    'doc_file' : values.doc_file,
                    'doc_name': values.doc_name,
                })
            return projectDocList

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj












