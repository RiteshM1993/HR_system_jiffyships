from hrms_employee.models import employee_experience


class employeeExperience:
    @classmethod
    def saveEmployeeExperience(cls, data, empId, created_by,created_date):
        try:
            for values in data:
                saveqry = employee_experience(emp_id=empId, prev_company_name=values['prevCompanyName'], job_title=values['jobTitle'], from_date=values['fromDate'], to_date=values['toDate'], job_description=values['jobDescription'], created_date=created_date, created_by=created_by)
                saveqry.save()
            successobj = {'data':'success'}
            return successobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def listingEmployeeExperience(cls, id):
        try:
            if id != 'undefined':
                listqry = employee_experience.objects.raw(
                    'select  emp_expr_id,prev_company_name,job_title,from_date,to_date,job_description, created_by  from employee_experience where  emp_id=' + id)

            else:
                listqry = employee_experience.objects.all()

            datalist = []
            for values in listqry:
                datalist.append({
                    'emp_expr_id': values.emp_expr_id,
                    'emp_id': values.emp_id,
                    'emp_name': ' '.join(filter(None, (values.first_name, values.middle_name, values.last_name))),
                    'prev_company_name': values.prev_company_name,
                    'job_title': values.job_title,
                    'from_date': values.from_date,
                    'to_date': values.to_date,
                    'job_description': values.job_description,
                    'created_by': values.created_by,
                })
            return datalist

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def deleteEmployeeExperience(cls,id):
        try:
            delqry = employee_experience.objects.get(emp_expr_id=id)
            delqry.delete()
            succesobj = {'data':'success'}
            return succesobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def geteditEmployeeExperiencedata(cls, id):
        try:
            getqry = employee_experience.objects.get(emp_expr_id=id)

            dataobj = {
                'emp_expr_id': getqry.emp_expr_id,
                'emp_id': getqry.emp_id,
                # 'emp_name': values.first_name+' '+values.middle_name+' '+values.last_name,
                'prev_company_name': getqry.prev_company_name,
                'job_title': getqry.job_title,
                'from_date': getqry.from_date,
                'to_date': getqry.to_date,
                'job_description': getqry.job_description
            }

            return dataobj


        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def updateEmployeeExperience(cls, id, prevCompanyName, jobTitle, fromDate, toDate, jobDescription, empId, updated_by,updated_date):
        try:
            getqry = employee_experience.objects.get(emp_expr_id=id)
            getqry.emp_id = empId
            getqry.prev_company_name = prevCompanyName
            getqry.job_title = jobTitle
            getqry.from_date = fromDate
            getqry.to_date = toDate
            getqry.job_description = jobDescription
            getqry.updated_by=updated_by
            getqry.updated_date=updated_date

            getqry.save()

            successobj = {'data': 'success'}

            return successobj

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj



