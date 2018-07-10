from hrms_employee.models import employee_education
from datetime import datetime


class dmemployeeeducation:

    @classmethod
    def listEmployeeeducation(self, id):
        try:
            if id != 'undefined':
                listqry = employee_education.objects.raw(
                    'select emp_edu_id,school_univeristy_name,qualification_degree_name,date_of_completion,notes from employee_education where emp_id=' + id)
            else:
                listqry = employee_education.objects.all()

            employeeeducationList = []

            for values in listqry:
                employeeeducationList.append({
                    'edu_id': values.emp_edu_id,
                    'emp_School_Univ_Name': values.school_univeristy_name,
                    'emp_Quali_Degr_Name': values.qualification_degree_name,
                    'emp_Doc': values.date_of_completion,
                    'emp_Notes': values.notes,
                })
            return employeeeducationList

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj

    def deleteemployeeducation(self,id):
        try:
            delqry = employee_education.objects.get(emp_edu_id=id)

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

    def getEmployeeeducationEditData(self,id):
        try:
            getqry = employee_education.objects.get(emp_edu_id=id)

            dataobj = {
                'edu_id': getqry.emp_edu_id,
                'empSchoolUniv_Name': getqry.school_univeristy_name,
                'empQuali_Degr_Name': getqry.qualification_degree_name,
                'empDoc':getqry.date_of_completion,
                'empNotes': getqry.notes,

                # 'dep_Relation': getqry.relation,

            }

            return dataobj

        except Exception, err:
            saveqryfailureobj = {
                'response': "Failure"
            }
            return saveqryfailureobj


    def updateemployeeEducation(cls, id,empSchoolUniv_Name,empQuali_Degr_Name,empDoc,empNotes,updated_by,updated_date):
        try:
            getqry = employee_education.objects.get(emp_edu_id=id)
            getqry.school_univeristy_name = empSchoolUniv_Name
            getqry.qualification_degree_name = empQuali_Degr_Name
            getqry.date_of_completion = empDoc
            getqry.notes = empNotes
            getqry.updated_by = updated_by
            getqry.updated_date= updated_date
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



    def saveempEdugrid(cls, Data,empid,created_by,created_date):
        try:
            for values in Data:
                saveqry = employee_education(emp_id=empid,school_univeristy_name =values['empSchoolUnivName'],
                                              qualification_degree_name=values['empQualiDegrName'], date_of_completion =values['empdateOfComplete'],
                                              notes=values['empNotes'], created_by=created_by,
                                             created_date=created_date)
                saveqry.save()
            successobj = {'data': 'success'}
            return successobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj
