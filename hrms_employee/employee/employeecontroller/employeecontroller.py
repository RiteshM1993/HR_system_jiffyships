import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from hrms_employee.employee.employeeservice.employeeservice import dmemployee
from datetime import datetime
from django.utils import timezone



@api_view(['POST'])
def saveEmployee(request):
    firstName = request.data['empFirstName']
    middleName = request.data.get('empMiddleName')
    lastName = request.data['empLastName']
    email = request.data['empEmail']
    empmobnum = request.data['empMobNum']
    empcurrentaddr = request.data['empCurrAddr']
    empperaddr = request.data['empPermaAddr']
    dmempid = request.data['dmEmpID']
    myfile = request.FILES['file']
    empexperience = request.data['experience']
    empRole = request.data['empRole']
    created_by = request.session['empId']
    created_date = datetime.now(tz=timezone.utc)

    dm_employee = dmemployee()

    result = dm_employee.saveEmployee(firstName, middleName,lastName, email, empmobnum,empcurrentaddr,empexperience, empperaddr,dmempid, myfile, empRole,created_date,created_by)



    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def listEmployee(request):
    dm_employee = dmemployee()

    result = dm_employee.listEmployee()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['DELETE'])
def delEmployee(request):
    id = request.GET['id']

    dm_employee = dmemployee()

    result = dm_employee.delEmployee(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def geteditdata(request):
    id = request.GET['id']
    dm_employee = dmemployee()

    result = dm_employee.geteditEmployeedata(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['POST'])
def updateEmployee(request):
    id = request.data['id']
    empFirstName = request.data['empFirstName']
    empMiddleName = request.data.get('empMiddleName')
    empLastName = request.data['empLastName']
    empEmail = request.data['empEmail']
    empMobNum = request.data['empMobNum']
    experience = request.data['experience']
    empCurrAddr = request.data['empCurrAddr']
    empPermaAddr = request.data['empPermaAddr']
    myfile = ''
    empRole = request.data['empRole']
    if request.FILES.get('file', False):
        myfile = request.FILES['file']

    updated_by = request.session['empId']
    updated_date = datetime.now(tz=timezone.utc)

    dm_employee = dmemployee()

    result = dm_employee.updateEmployee(id, empFirstName, empMiddleName, empLastName, empEmail,empMobNum,experience,empCurrAddr, empPermaAddr, myfile,empRole,updated_date,updated_by)


    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

