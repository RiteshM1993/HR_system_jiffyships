from hrms_admin.models import billing

from hrms_admin.models import project_master

class Billing:
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
    def savebilling(self, project_id,startDate,endDate,billresourceCount,totalBill,createdby,createdDate):
        try:
            saveqry = billing(project_id=project_id,start_date =startDate,end_date=endDate,billable_resource_count =billresourceCount, total_bill =totalBill,created_by=createdby,created_date=createdDate)

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
    def listbilling(cls):
        try:
            # listqry = employee_experience.objects.raw('select a.emp_id, a.emp_expr_id,a.prev_company_name,a.job_title,a.from_date,a.to_date, a.job_description, a.created_by, b.first_name, b.middle_name, b.last_name from employee_experience a inner join employee b on a.emp_id=b.emp_id')
            listqry = billing.objects.raw('select a.bill_id, a.project_id,a.billable_resource_count,a.total_bill,b.project_id,b.project_name from billing a inner join project_master b on a.project_id=b.project_id')
            datalist = []
            for values in listqry:
                datalist.append({
                    'project_id': values.project_id,
                    'project_name':values.project_name,
                    'billable_resource_count': values.billable_resource_count,
                    'total_bill':values.total_bill,
                    'start_date': values.start_date ,
                    'end_date': values.end_date,
                    # 'empcount': values.empcount,
                    # 'rate_per_hour': values.rate_per_hour,
                })
            return datalist

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj

    @classmethod
    def generatebilling(cls):
        try:
            listqry=project_master.objects.raw('select count(0) empcount,  count(0) * a.rate_per_hour bill_amount,a.project_id from project_master a inner join employee_project b on a.project_id = b.project_id where a.project_id=5 group by a.project_id')
            datalist=[]
            for values in listqry:
                datalist.append({
                    'project_id': values.project_id,
                    'empcount':values.empcount,
                    'rate_per_hour':values.rate_per_hour,

                })
            return  datalist

        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj
