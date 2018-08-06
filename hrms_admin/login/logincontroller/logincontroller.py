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

