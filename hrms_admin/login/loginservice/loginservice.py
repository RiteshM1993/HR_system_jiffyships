from hrms_employee.models import employee
# from pprint import pprint
# from django.contrib import sessions

from django.contrib.sessions.models import Session




#
class dmlogin:
    @classmethod
    def login(cls, email_id):
        try:
            getqry=employee.objects.get(email_id=email_id)

            if getqry.email_id:
                succesresplist= []
                succesresplist.append({
                    'empid': getqry.emp_id,
                    'emailid':getqry.email_id,
                    'emp_name': ' '.join(filter(None, (getqry.first_name, getqry.middle_name, getqry.last_name))),
                    'emp_role': getqry.emp_role,
                    'emp_img': getqry.emp_image,
                })

                return {'data':succesresplist}

            else:
                return {'errorResp':'Error'}


        except Exception, err:
            failureobj = {
                'response': "Failure"
            }
            return failureobj



    # def checkSession(request):
    #
    #     # pprint (request)
    #
    #     # if  request.session['emailId']:
    #     #     emailId = request.session['emailId']
    #     #     dataobj = {
    #     #         'data': True
    #     #     }
    #     # else:
    #     #     dataobj = {
    #     #         'data': False
    #     #     }
    #
    #     dataobj = {
    #            'data': ''#request.session.has_key('emailId')
    #          }
    #     return dataobj
