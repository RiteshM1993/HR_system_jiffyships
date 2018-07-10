from hrms_admin.models import designationmaster


class dmdesignation:
    @classmethod
    def saveDesignation(self, designationName,created_by,created_date):
        try:
            saveqry = designationmaster(designation_name=designationName,created_by=created_by,created_date=created_date)
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
    def listDesignation(self):
        try:
            listqry = designationmaster.objects.all()
            designationList = []

            for values in listqry:
                designationList.append({
                    'des_id' : values.designation_id,
                    'des_name' : values.designation_name,
                })
            return designationList

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def deleteDesignation(self, id):
        try:
            delqry = designationmaster.objects.get(designation_id=id)
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
    def geteditDesignationdata(cls,id):
        try:
            getqry = designationmaster.objects.get(designation_id=id)
            dataobj = {
                'des_id': getqry.designation_id,
                'des_name': getqry.designation_name,
            }
            return dataobj
        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def updateDesignation(self, id, designationName,updated_by,updated_date):
        try:
            getqry = designationmaster.objects.get(designation_id=id)

            getqry.designation_name = designationName
            getqry.updated_date=updated_date
            getqry.updated_by=updated_by

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




