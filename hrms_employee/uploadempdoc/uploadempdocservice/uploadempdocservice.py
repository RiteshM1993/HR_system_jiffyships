from hrms_employee.models import employee_doc
from django.core.files.storage import FileSystemStorage


class empDoc:
    @classmethod
    def saveEmpDoc(cls,doc_name,doc_file,empid,created_date,created_by):
        try:
            saveqry = employee_doc(emp_id=empid,doc_name=doc_name,upload_doc_name=doc_file.name,created_by=created_by,created_date=created_date)
            saveqry.save()

            fs = FileSystemStorage("static/dist/empdocs/")

            fs.save(doc_file.name, doc_file)

            successobj = {'data':'success'}
            return successobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def listingEmpDoc(cls):
        try:
            listqry = employee_doc.objects.all()
            datalist = []
            for values in listqry:
                datalist.append({
                    'docId' : values.docId,
                    'emp_id' : values.emp_id,
                    'doc_name': values.doc_name,
                    'upload_doc_name': values.upload_doc_name,
                })
            return datalist

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def deleteEmpDoc(cls,id):
        try:
            delqry = employee_doc.objects.get(docId=id)
            delqry.delete()
            dataobj = {'data':'success'}
            return dataobj

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
    #
    # @classmethod
    # def updateEmpdoc(cls,id,docName,doc_file,modifiedDate):
    #     try:
    #         updateqry = employee_doc.objects.get(docId=id)
    #         updateqry.doc_name = docName
    #         updateqry.upload_doc_name = doc_file.name
    #         updateqry.modified_date = modifiedDate
    #
    #         updateqry.save()
    #
    #         fs = FileSystemStorage("static/dist/empdocs/")
    #
    #         fs.save(doc_file.name, doc_file)
    #
    #         dataobj = {'data':'success'}
    #
    #         return dataobj
    #
    #     except Exception, err:
    #         failureobj = {
    #             'response': "Failure"
    #         }
    #         return failureobj

    @classmethod
    def updateEmpdoc(cls, id,docName, doc_file, updated_by,updated_date):
        try:
            updateqry = employee_doc.objects.get(docId=id)
            updateqry.doc_name = docName
            if doc_file != 'undefined':
                # updateqry.doc_name = doc_name
                updateqry.upload_doc_name = doc_file.name
                fs = FileSystemStorage("static/dist/empdocs/")

                fs.save(doc_file.name, doc_file)

            updateqry.updated_date = updated_date
            updateqry.updated_by = updated_by

            updateqry.save()

            dataobj = {'data': 'success'}

            return dataobj


        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj





