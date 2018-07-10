from hrms_employee.models import employee_doc
from hrms_employee.models import employee
from django.core.files.storage import FileSystemStorage


class employeeResign:
    @classmethod
    def saveEmpResignation(cls,resignReason,resignDate,emp_id,dateofleaving,updated_by,updated_date ):
        try:

            getqry = employee.object.get(emp_id=emp_id)

            getqry.reason_of_leaving = resignReason
            getqry.resignation_date = resignDate
            getqry.updated_date = updated_date
            getqry.updated_by = updated_by
            getqry.date_of_leaving = dateofleaving
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
            listqry = employee_doc.objects.raw('Select emp_id,date_of_leaving,resignation_date,reason_of_leaving,first_name, middle_name, last_name from employee')
            datalist = []
            for values in listqry:
                datalist.append({
                    'dol' : values.date_of_leaving,
                    'resignReason' : values.reason_of_leaving,
                    'resignDate': values.resignation_date,
                    'emp_id': values.upload_doc_name,
                    'emp_name' : ' '.join(filter(None, (values.first_name, values.middle_name, values.last_name))),
                })
            return datalist

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj


    @classmethod
    def getEmpeditDocdata(cls, id):
        try:
            getdataqry = employee_doc.objects.get(docId=id)

            dataobj = {
                'docId' : getdataqry.docId,
                'doc_name': getdataqry.doc_name,
                'upload_doc_name': getdataqry.upload_doc_name,
            }

            return dataobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def updateEmpdoc(cls,id,docName,doc_file,modifiedDate):
        try:
            updateqry = employee_doc.objects.get(docId=id)

            updateqry.doc_name = docName
            updateqry.upload_doc_name = doc_file.name
            updateqry.modified_date = modifiedDate

            updateqry.save()

            fs = FileSystemStorage("static/dist/empdocs/")

            fs.save(doc_file.name, doc_file)

            dataobj = {'data':'success'}

            return dataobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj







