import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
# from hrms_employee.employee.employeeservice.employeeservice import dmlogin
# from hrms_admin.login.loginservice.loginservice import EmailBackend
from hrms_admin.login.loginservice.loginservice import dmlogin
import time
from datetime import datetime
from django.utils import timezone

from django.contrib import sessions


@api_view(['POST'])
def login(request):
    email_id = request.data['emailid']

    dm_login = dmlogin()

    result = dm_login.login(email_id)

    request.session['emailId'] = result['data'][0]['emailid']
    request.session['empId'] = result['data'][0]['empid']
    request.session['empRole'] = result['data'][0]['emp_role']
    request.session['empImg'] = result['data'][0]['emp_img']
    request.session['empName'] = result['data'][0]['emp_name']

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)



@api_view(['GET'])
def checksession(request):
    if (request.session.has_key('emailId')):
        dataobj = {
            'email_id': request.session["emailId"],
            'empId': request.session["empId"],
            'empRole': request.session["empRole"],
            'mes':'session created',
            'empImg': request.session["empImg"],
            'empName': request.session['empName'],

        }
    else:
        dataobj ={'data': '', 'mes':'No Session'}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def logout(request):
    request.session['emailId'] = ''
    request.session['empId'] = ''
    request.session['empRole'] = ''
    request.session['empImg'] = ''
    dataobj = {'msg':'logout'}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


# client_id = "81no80w1kjjjjr"
# client_secret = "VWGAG1LLkK2jRoDh"
# authorization_base_url = 'https://www.linkedin.com/uas/oauth2/authorization'
# token_url = 'https://www.linkedin.com/uas/oauth2/accessToken'
# from requests_oauthlib import OAuth2Session
# from requests_oauthlib.compliance_fixes import linkedin_compliance_fix
# linkedin = OAuth2Session(client_id, redirect_uri='http://127.0.0.1')
# linkedin = linkedin_compliance_fix(linkedin)
# authorization_url, state = linkedin.authorization_url(authorization_base_url)
# red='http://127.0.0.1/?code=AQR8xgjm-y0WGp2yld9WqDLosv1upChkZp7nq7JMJZtdcDpovqrt-Rwi34I4OSQMVuq-bdUyvy6RbJMWyv7u6DBOaLgIxQ_mZpUt2G-Pr9GZMLi5xH5aFj7kzD9pe2zBrNWJs0VG0MclBaUBuY3iDAi1cxGamw&state=WjaloaCyfCDoUznPZERZb9abLaCREK#!'
# r = linkedin.get('https://api.linkedin.com/v1/people/~')
# token = linkedin.fetch_token(token_url='https://www.linkedin.com/uas/oauth2/accessToken', client_id=client_id,client_secret=client_secret,code='AQSS6xjj16IAHiqaWzbMpXYlYrLclvFsj3NIEzVQgC1e058lU9N7oMbLe8iPbz-EfVYXTu-6mmSgeB_Rkv0GTP6GFuTbrRDR43IO7hg-ExCXuOVbZeHQmI8AjNUgZto78TA8hynd0sAyx3nrH7ZOE47pARnr7g')
# r = linkedin.get('https://api.linkedin.com/v1/people/~')
# r.content