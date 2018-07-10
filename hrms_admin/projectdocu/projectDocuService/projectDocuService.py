from hrms_admin.models import project_documents
from django.core.files.storage import FileSystemStorage

from hrms_admin.projectmaster.projectmasterservice.projectmasterservice import dmprojectmaster

from hrms_admin.models import project_master

class projDoc:
    @classmethod
    def saveProjDoc(cls, project_id,doc_name,doc_file,createdby,createdDate):
        try:
            saveqry = project_documents(project_id=project_id, doc_name=doc_name, doc_file=doc_file.name,created_by=createdby,
            created_date=createdDate)
            saveqry.save()

            fs = FileSystemStorage("static/dist/projdocs/")

            fs.save(doc_file.name, doc_file)

            successobj = {'data': 'success'}
            return successobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def projectnamevalues(self):
        try:
            listqry = project_master.objects.all()
            projectnamelist = []

            for values in listqry:
                projectnamelist.append({
                    'project_id': values.project_id,
                    'project_name': values.project_name,

                })

            return projectnamelist

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def listProjDoc(self):
        try:
            listqry = project_documents.objects.raw('select a.proj_doc_id, a.project_id,a.doc_name,a.doc_file,b.project_id,b.project_name from project_documents a inner join project_master b on a.project_id=b.project_id')
            projectDocList = []

            for values in listqry:
                projectDocList.append({
                    'proj_doc_id':values.proj_doc_id,
                    'project_id': values.project_id,
                    'project_name': values.project_name,
                    'doc_name':values.doc_name,
                    'doc_file':values.doc_file

                })
            # return {'data':projectDocList}
            return projectDocList


        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def deleteProjDoc(cls, id):
        try:
            delqry = project_documents.objects.get( proj_doc_id =id)
            delqry.delete()
            dataobj = {'data': 'success'}
            return dataobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj



    @classmethod
    def getEditProjdoc(self, id):
        try:
            dataobj = {
            }
            # getqry = employee_project.objects.get(emp_proj_id=id)
            getqry = project_documents.objects.raw('select a.proj_doc_id, a.project_id,a.doc_name,a.doc_file,b.project_id,b.project_name from project_documents a inner join project_master b on a.project_id=b.project_id where a.proj_doc_id='+id)
            for data in getqry:
                dataobj = {
                    'proj_doc_id': data.proj_doc_id,
                    'project_id':data.project_id,
                    'project_name': data.project_name,
                    'doc_name': data.doc_name,
                    'doc_file': data.doc_file,
                }

            return dataobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def updateProjdoc(cls, id,project_id,doc_name,doc_file,updated_by,updated_date):
        try:
            updateqry = project_documents.objects.get(proj_doc_id=id)
            updateqry.project_id=project_id
            if doc_file != 'undefined':
                # updateqry.doc_name = doc_name
                updateqry.doc_file = doc_file.name
                fs = FileSystemStorage("static/dist/projdocs/")

                fs.save(doc_file.name, doc_file)

            updateqry.doc_name = doc_name
            updateqry.updated_by=updated_by
            updateqry.updated_date = updated_date
            updateqry.save()

            dataobj = {'data': 'success'}

            return dataobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    # @classmethod
    # def updateProjdoc(cls, id, project_id, doc_name, doc_file, createdby, createdDate):
    #     try:
    #         updateqry = project_documents.objects.get(proj_doc_id=id)
    #         updateqry.project_id = project_id
    #         if doc_file != 'undefined':
    #             updateqry.doc_name = doc_name
    #             updateqry.doc_file = doc_file.name
    #             fs = FileSystemStorage("static/dist/projdocs/")
    #
    #             fs.save(doc_file.name, doc_file)
    #             updateqry.created_by = createdby
    #             updateqry.created_date = createdDate
    #             updateqry.save()
    #
    #             dataobj = {'data': 'success'}
    #
    #             return dataobj
    #         else:
    #             updateqry.doc_name = doc_name
    #             updateqry.doc_file = doc_file.name
    #             fs = FileSystemStorage("static/dist/projdocs/")
    #
    #             fs.save(doc_file.name, doc_file)
    #             updateqry.created_by = createdby
    #             updateqry.created_date = createdDate
    #             updateqry.save()
    #
    #             dataobj = {'data': 'success'}
    #
    #             return dataobj
    #
    #     except Exception, err:
    #         failureobj = {
    #             'response': "Failure"
    #         }
    #         return failureobj








