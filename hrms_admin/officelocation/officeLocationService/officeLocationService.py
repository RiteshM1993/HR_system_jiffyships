from hrms_admin.models import office_location

class officeLocation:
    @classmethod
    def saveOfficeLocation(self, officelocation, address, created_date, created_by):
        try:
            saveqry = office_location(office_location = officelocation, address =address, created_date = created_date, created_by=created_by)
            saveqry.save()
            successobj = {'data': 'success'}
            return successobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def listOfficelocaltion(self):
        try:
            saveqry = office_location.objects.all()
            datalist = []
            for values in saveqry:
                datalist.append({
                    'locationId' : values.location_id,
                    'officeLocation' : values.office_location,
                    'address' : values.address,
                    'createdDate' : values.created_date,
                })
            return datalist

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def deleteOfficelocaltion(self,id):
        try:
            delqry = office_location.objects.get(location_id=id)
            delqry.delete()
            dataobj = {
                'response': "success"
            }

            return dataobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def geteditofficelocaltion(self,id):
        try:
            getqry = office_location.objects.get(location_id=id)
            dataobj = {
                'locationId' : getqry.location_id,
                'officeLocation' : getqry.office_location,
                'address' : getqry.address,
                'createdDate' : getqry.created_date,
            }

            return dataobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def updateOfficeLocation(self, id, officelocation, address, updated_by,updated_date):
        try:
            getqry = office_location.objects.get(location_id=id)

            getqry.office_location = officelocation
            getqry.address = address
            getqry.updated_date = updated_date
            getqry.updated_by = updated_by
            getqry.save()
            successobj = {'data': 'success'}
            return successobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj
