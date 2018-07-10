from hrms_admin.models import projecttypemaster

class dmprojecttype:
    @classmethod
    def saveProjecttype(self, projecttypeName,created_by,created_date):
        try:
            saveqry = projecttypemaster(project_type_name=projecttypeName,created_by=created_by,created_date=created_date)
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
    def listProjecttype(self):
        try:
            listqry = projecttypemaster.objects.all()
            projecttypeList = []

            for values in listqry:
                projecttypeList.append({
                    'proj_id': values.proj_typemaster_id,
                    'proj_name': values.project_type_name,
                })
            return projecttypeList

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj



    @classmethod
    def deleteProjecttype(self, id):
        try:
            delqry = projecttypemaster.objects.get(proj_typemaster_id=id)
            delqry.delete()
            successobj = {
                'successmsg': "success",
            }
            return successobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def geteditProjecttypedata(cls, id):
        try:
            getqry = projecttypemaster.objects.get(proj_typemaster_id=id)
            dataobj = {
                'proj_id': getqry.proj_typemaster_id,
                'proj_name': getqry.project_type_name,
            }
            return dataobj
        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def updateProjecttype(self, id, projecttypeName,updated_by,updated_date):
        try:
            getqry = projecttypemaster.objects.get(proj_typemaster_id=id)
            getqry.project_type_name = projecttypeName
            getqry.updated_by= updated_by
            getqry.updated_date= updated_date

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




