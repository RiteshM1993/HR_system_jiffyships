from hrms_employee.models import employee_type


class empType:
    @classmethod
    def saveEmpType(cls,empTypeName,created_date,created_by):
        try:
            saveqry = employee_type(type_name=empTypeName,created_date=created_date,created_by=created_by)
            saveqry.save()
            successobj = {'data':'success'}
            return successobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def listingEmpType(cls):
        try:
            listqry = employee_type.objects.all()
            datalist = []
            for values in listqry:
                datalist.append({
                    'emp_type_id' : values.emp_typeId,
                    'type_name' : values.type_name,
                })
            return datalist

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def deleteEmpType(cls,typeid):
        try:
            delqry = employee_type.objects.get(emp_typeId=typeid)
            delqry.delete()
            dataobj = {'data':'success'}
            return dataobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def getEmpTypedata(cls, typeid):
        try:
            getdataqry = employee_type.objects.get(emp_typeId=typeid)

            dataobj = {
                'id' : getdataqry.emp_typeId,
                'type_name' : getdataqry.type_name,
            }

            return dataobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def updateEmpTypedata(cl,typeId,typeName,updated_date,updated_by):
        try:
            updateqry = employee_type.objects.get(emp_typeId=typeId)

            updateqry.type_name = typeName
            updateqry.updated_date=updated_date
            updateqry.updated_by=updated_by

            updateqry.save()

            dataobj = {'data':'success'}

            return dataobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj







