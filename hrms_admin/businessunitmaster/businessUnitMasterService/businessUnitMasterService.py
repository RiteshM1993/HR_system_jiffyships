from hrms_admin.models import businessunitmaster
from hrms_employee.models import employee


class businessUnitMaster:
    @classmethod
    def addBusinessUnitMaster(cls, business_name, business_parent, status, managerId,created_by,created_date):
        try:
            if not managerId:
                saveqry = businessunitmaster(bu_name=business_name, bu_parentid=business_parent, active=status, created_by=created_by,created_date=created_date)
                saveqry.save()
            else:
                for values in managerId:
                    saveqry = businessunitmaster(bu_name=business_name, bu_parentid=business_parent, active=status, bu_manager_id=values, created_by=created_by,created_date=created_date)
                    saveqry.save()
            saveqryobj = {
                'response': "success"
            }
            return saveqryobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    @classmethod
    def listBusinessUnitMaster(self):
        try:
            getqry = businessunitmaster.objects.raw('Select a.bu_id,a.bu_name,a.bu_parentid,a.active,b.emp_id,b.first_name,b.middle_name,b.last_name from business_unit_master a left join employee b on a.bu_manager_id=b.emp_id')
            datalist = []
            for values in getqry:
                getparentnameqry = None
                data_dict = {
                    'business_id': values.bu_id,
                    'business_name': values.bu_name,
                    'business_parent': None,
                    'bu_parentid': None,
                    'status': values.active,
                    'manager_id': values.emp_id,
                    'manager_name': ' '.join(filter(None, (values.first_name , values.middle_name , values.last_name)))
                }

                if values.bu_parentid is not None:
                    getparentnameqry = businessunitmaster.objects.get(bu_id=values.bu_parentid)
                    data_dict['business_parent'] = getparentnameqry.bu_name
                    data_dict['bu_parentid'] = getparentnameqry.bu_parentid
                datalist.append(data_dict)
            return datalist
        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def delBusinessUnitMaster(self, id):
        try:
            delqry = businessunitmaster.objects.get(bu_id=id)
            delqry.delete()
            successobj = {
                'response': "success"
            }
            return successobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def geteditdata(self, id):
        try:
            getqry = businessunitmaster.objects.raw('Select a.bu_id,a.bu_name,a.bu_parentid,a.active,b.emp_id,b.first_name,b.middle_name,b.last_name from business_unit_master a left join employee b on a.bu_manager_id=b.emp_id where bu_id='+id)

            dataobj = {
                'business_id': getqry[0].bu_id,
                'business_name': getqry[0].bu_name,
                'business_parent': getqry[0].bu_parentid,
                'status': getqry[0].active,
                'bu_manager_id': getqry[0].bu_manager_id,
                'manager_name': ' '.join(filter(None, (getqry[0].first_name, getqry[0].middle_name, getqry[0].last_name)))
            }

            return dataobj

        except Exception, err:

            failureobj = {
                'response': "Failure"
            }

            return failureobj

    @classmethod
    def updateBusinessUnitMaster(cls, id, business_name, business_parent, status,managerId,updated_by, updated_date):
        try:
            getqry = businessunitmaster.objects.get(bu_id=id)
            if managerId:
                for values in managerId:
                    getqry.bu_manager_id=values
                    getqry.bu_name = business_name
                    getqry.bu_parentid = business_parent
                    getqry.active = status
                    getqry.updated_by = updated_by
                    getqry.updated_date = updated_date
                    getqry.save()
            else:
                getqry.bu_name = business_name
                getqry.bu_parentid = business_parent
                getqry.active = status
                getqry.updated_by = updated_by
                getqry.updated_date = updated_date
                getqry.save()

            saveqryobj = {
                'response': "success"
            }
            return saveqryobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj
