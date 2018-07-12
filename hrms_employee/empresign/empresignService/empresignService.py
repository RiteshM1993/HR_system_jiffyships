from hrms_employee.models import employee_doc
from hrms_employee.models import employee
from django.core.files.storage import FileSystemStorage


class employeeResign:
    @classmethod
    def saveEmpResignation(cls,resignReason,resignDate,emp_id,dateofleaving,updated_by,updated_date,resign_status):
        try:

            getqry = employee.object.get(emp_id=emp_id)

            getqry.reason_of_leaving = resignReason
            getqry.resignation_date = resignDate
            getqry.updated_date = updated_date
            getqry.updated_by = updated_by
            getqry.date_of_leaving = dateofleaving
            getqry.resign_status = resign_status
            getqry.save()

            successobj = {'data':'success'}
            return successobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def listingEmpresign(cls):
        try:
            listqry = employee.objects.raw('Select emp_id,date_of_leaving,resignation_date,reason_of_leaving,first_name, middle_name, last_name from employee where resign_status=1 order by resignation_date')
            datalist = []
            for values in listqry:
                datalist.append({
                    'dol' : values.date_of_leaving,
                    'resignReason' : values.reason_of_leaving,
                    'resignDate': values.resignation_date,
                    'emp_id': values.emp_id,
                    'emp_name' : ' '.join(filter(None, (values.first_name, values.middle_name, values.last_name))),
                })
            return datalist

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def getEmpeResigndata(cls, id):
        try:
            getdataqry = employee.objects.get(emp_id=id)

            dataobj = {
                # 'emp_name' : getdataqry.emp_name,
                'resignation_date': getdataqry.resignation_date,
                'reason_of_leaving': getdataqry.reason_of_leaving,
            }

            return dataobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj



    @classmethod
    def updateEmpeResignData(cls,id,resignReason,resignDate,managerComment,updatedDate):
        try:
            updateqry = employee.objects.get(emp_id=id)
            updateqry.reason_of_leaving = resignReason
            updateqry.resignation_date = resignDate
            updateqry.manager_resignation_comment = managerComment
            updateqry.updated_date = updatedDate
            updateqry.save()

            dataobj = {'data':'success'}

            return dataobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def geteditdata(cls, id):
        try:
            getqry = employee.objects.get(emp_id=id)
            dataobj = {
                'managerComment':getqry.manager_resignation_comment,
                'emp_id': getqry.emp_id,
                'dol': getqry.date_of_leaving,
                'resignDate': getqry.resignation_date,
                'reasonResign': getqry.reason_of_leaving,
                # 'emp_name': ' '.join(filter(None, (getqry.first_name, getqry.middle_name, getqry.last_name))),
            }
            return dataobj
        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj







