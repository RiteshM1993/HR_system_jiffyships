import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from hrms_employee.employeeproject.employeeprojectservice.employeeprojectservice import dmemployeeproject
from datetime import datetime
from django.utils import timezone

@api_view(['POST'])
def saveEmployeeprojecttype(request):
    emp_id=request.data['emp_id']
    project_id = request.data['project_id']
    start_Date = request.data['startDate']
    end_Date=request.data['endDate']
    empdesc = request.data['empdesc']
    created_by = request.session['empId']
    created_date = datetime.now(tz=timezone.utc)

    dm_employeeproject = dmemployeeproject()

    result = dm_employeeproject.saveEmployeeproject(emp_id,project_id,start_Date,end_Date,empdesc,created_by,created_date)

    dataobj ={'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def employeename(request):
    name=request.GET['name']
    dm_employeeproject = dmemployeeproject()

    result = dm_employeeproject.listemployeevalues(name)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def listEmployeeproject(request):
    dm_employeeproject = dmemployeeproject()

    result = dm_employeeproject.listEmployeeproject()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['DELETE'])
def deleteEmployeeproject(request):
    id = request.GET['id']

    dm_employeeproject = dmemployeeproject()

    result = dm_employeeproject.deleteemployeeproject(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def geteditdata(request):

    id = request.GET['id']

    dm_employeeproject = dmemployeeproject()

    result = dm_employeeproject.getEmployeeprojectdata(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['POST'])
def updateEmployeeproject(request):
    id = request.data['id']
    emp_id = request.data['emp_id']
    project_id = request.data['project_id']
    start_Date = request.data['start_date']
    end_Date = request.data['end_date']
    emp_desc = request.data['emp_desc']
    updated_by = request.session['empId']
    updated_date = datetime.now(tz=timezone.utc)

    dm_employeeproject = dmemployeeproject()

    result = dm_employeeproject.updateemployeeproject(id,emp_id ,project_id,start_Date,end_Date,emp_desc,updated_by,updated_date)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def projecttype(request):
    dm_employeeproject = dmemployeeproject()

    result = dm_employeeproject.projectmastertypevalues()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def getResources(request):
    id = request.GET['id']
    dm_employeeproject = dmemployeeproject()

    result = dm_employeeproject.getResourceData(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def getStartEndDate(request):
    id = request.GET['id']
    dm_employeeproject = dmemployeeproject()

    result = dm_employeeproject.getStartEndDateData(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def getDocuments(request):
    id = request.GET['id']
    dm_employeeproject = dmemployeeproject()

    result = dm_employeeproject.getProjectDocument(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


