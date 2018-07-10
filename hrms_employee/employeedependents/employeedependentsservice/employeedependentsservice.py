from hrms_employee.models import employee_dependents
from datetime import datetime

class dmemployeedependents:
    @classmethod
    def saveEmployeedependents(self, emp_Dep_Name,emp_Dob,emp_Relation,empid,created_by,created_date):
        try:

            saveqry = employee_dependents(dependent_name=emp_Dep_Name,dob=emp_Dob,relation=emp_Relation,emp_id=empid,created_by=created_by,created_date=created_date)

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
    def listEmployeedependents(self, id):
        try:
            if id != 'undefined':
                listqry = employee_dependents.objects.raw(
                    'select dependent_id,dependent_name, dob,relation from employee_dependents where emp_id=' + id)
            else:
                listqry = employee_dependents.objects.all()

            employeedependentsList = []

            for values in listqry:
                employeedependentsList.append({
                    'dep_id': values.dependent_id,
                    'emp_id': values.emp_id,
                    'emp_dep_name': values.dependent_name,
                    'emp_relation': values.relation,
                    'emp_dob': values.dob
                })
            return employeedependentsList

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj


    def deleteEmployeedependents(self,id):
        try:
            delqry = employee_dependents.objects.get(dependent_id=id)

            delqry.delete()
            saveqrysuccessobj = {
                'response': "success"
            }
            return saveqrysuccessobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    def getEmployeedependentsEditData(self,id):
        try:
            getqry = employee_dependents.objects.get(dependent_id=id)

            dataobj = {
                'dep_id': getqry.dependent_id,
                'dep_name': getqry.dependent_name,
                'dep_Relation': getqry.relation,
                'dep_dob':getqry.dob,
                # 'dep_Relation': getqry.relation,

            }

            return dataobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj


    def updateEmployeedependents(cls, id, dep_Name, dep_Relation, dep_dob,updated_by,updated_date):
        try:
            getqry =employee_dependents.objects.get(dependent_id=id)
            getqry.dependent_name=dep_Name
            getqry.relation=dep_Relation
            getqry.dob=dep_dob
            getqry.updated_by=updated_by
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

