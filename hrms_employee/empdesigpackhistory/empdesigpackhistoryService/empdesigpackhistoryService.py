from hrms_employee.models import employee_designationpackagehistory
from hrms_employee.models import employee
from hrms_admin.models import currencymaster

class employeeHistory:
    @classmethod
    def getEmployeeName(cls):
        try:
            getnameqry = employee.objects.all()
            datalist = []
            for values in getnameqry:
                datalist.append({
                    'emp_id' : values.emp_id,
                    'emp_name' : values.first_name+' '+values.middle_name+' '+values.last_name,
                })
            return datalist
        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj


    @classmethod
    def getcurrency(cls):
        try:
            getcurrencyqry = currencymaster.objects.all()
            datalist = []
            for values in getcurrencyqry:
                datalist.append({
                     'currency_id' : values.currency_id,
                     'currency_name' : values.currency_name,
                     'currency_logo' : values.currency_logo,
                })
            return datalist
        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def saveEmployeeDesignPackHistory(self,emp_id,salary,from_date,active,currency_id,designation_id,created_date, created_by):
        try:
            saveempdesigpackhist= employee_designationpackagehistory(emp_id=emp_id,salary=salary,from_date=from_date,created_date=created_date,active=active,currency_id=currency_id, designation_id=designation_id, created_by=created_by)
            saveempdesigpackhist.save()
            dataobj = {'data':'success'}
            return dataobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def listingEmployeeDesignPackHistory(cls, id):
        try:
            if id != 'undefined':
                getEmployeeDesignPackHistory = employee_designationpackagehistory.objects.raw(
                    'select a.emp_id,d.first_name,d.middle_name,d.last_name,b.currency_name,b.currency_logo,a.currency_id,a.designation_id,a.active,a.pckg_id,a.emp_id,a.salary,a.from_date, a.created_by, c.designation_name from employee_designationpackagehistory a inner join currency_master b on a.currency_id=b.currency_id inner join designation_master c on a.designation_id=c.designation_id inner join employee d on a.emp_id=d.emp_id where a.active=1 and a.emp_id=' + id)

            else:
                getEmployeeDesignPackHistory = employee_designationpackagehistory.objects.raw(
                    'select a.emp_id,d.first_name,d.middle_name,d.last_name,b.currency_name,b.currency_logo,a.currency_id,a.designation_id,a.active,a.pckg_id,a.emp_id,a.salary,a.from_date, a.created_by, c.designation_name from employee_designationpackagehistory a inner join currency_master b on a.currency_id=b.currency_id inner join designation_master c on a.designation_id=c.designation_id inner join employee d on a.emp_id=d.emp_id where a.active=1')

            datalist = []

            for values in getEmployeeDesignPackHistory:
                if values.middle_name is None:
                    values.middle_name = ''
                datalist.append({
                    'pckg_id': values.pckg_id,
                    'emp_id': values.emp_id,
                    'emp_name': values.first_name + ' ' + values.middle_name + ' ' + values.last_name,
                    'salary': values.salary,
                    'from_date': values.from_date,
                    # 'to_date' : values.to_date,
                    'created_by': values.created_by,
                    'active': values.active,
                    'currencyid': values.currency_id,
                    'currencyname': values.currency_name,
                    'currency_logo': values.currency_logo,
                    'designation_id': values.designation_id,
                    'designation_name': values.designation_name,
                })

            return datalist

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def deleteEmployeeDesignPackHistory(self,id):
        try:
            delqry = employee_designationpackagehistory.objects.get(pckg_id=id)

            delqry.delete()

            dataobj = {'data':'success'}

            return dataobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def EmployeeDesignPackHistoryEditData(cls,id):
        try:
            geteditdataqry = employee_designationpackagehistory.objects.raw('select a.emp_id,d.first_name,d.middle_name,d.last_name,b.currency_name,b.currency_logo,a.currency_id,a.designation_id,a.active,a.pckg_id,a.emp_id,a.salary,a.from_date, a.created_by, c.designation_name from employee_designationpackagehistory a inner join currency_master b on a.currency_id=b.currency_id inner join designation_master c on a.designation_id=c.designation_id inner join employee d on a.emp_id=d.emp_id where a.pckg_id='+id)

            datalist = []

            for values in geteditdataqry:
                if values.middle_name is None:
                    values.middle_name =''
                datalist.append({
                    'pckg_id': values.pckg_id,
                    'emp_id': values.emp_id,
                    'emp_name': values.first_name + ' ' + values.middle_name + ' ' + values.last_name,
                    'salary': values.salary,
                    'from_date': values.from_date,
                    # 'to_date': values.to_date,
                    'created_by': values.created_by,
                    'active': values.active,
                    'currencyid': values.currency_id,
                    'currencyname': values.currency_name,
                    'currency_logo': values.currency_logo,
                    'designationId': values.designation_id,
                    'designation_name': values.designation_name,
                })

            return datalist

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def updateEmployeeDesignPackHistory(self,empdesigpack_id,emp_id, salary, from_date, active, currency_id,
                                                            designation_id, updated_date, updated_by):
        try:
            getdataqry = employee_designationpackagehistory.objects.get(pckg_id=empdesigpack_id)

            getdataqry.active = 0

            getdataqry.save()

            saveqry= employee_designationpackagehistory(emp_id=emp_id, salary=salary, from_date=from_date,
                                                                      updated_date=updated_date, active=active,
                                                                      currency_id=currency_id,
                                                                      designation_id=designation_id,
                                                                      updated_by=updated_by)
            saveqry.save()
            dataobj = {'data': 'success'}
            return dataobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj


