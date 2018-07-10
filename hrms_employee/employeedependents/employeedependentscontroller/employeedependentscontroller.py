import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from hrms_employee.employeedependents.employeedependentsservice.employeedependentsservice import dmemployeedependents
from datetime import datetime
from django.utils import timezone

@api_view(['POST'])
def saveEmployeedependents(request):
    emp_Dep_Name = request.data['emp_DependentsName']
    emp_Dob = request.data['emp_Dob']
    emp_Relation = request.data['emp_Relation']
    empid=request.session['empId']
    created_by = request.session['empId']
    created_date = datetime.now(tz=timezone.utc)

    dm_employeedependents = dmemployeedependents()

    result = dm_employeedependents.saveEmployeedependents(emp_Dep_Name,emp_Dob,emp_Relation,empid,created_by,created_date)

    dataobj ={'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)



@api_view(['GET'])
def listEmployeedependents(request):
    dm_employeedependents = dmemployeedependents()
    # id = request.get('id')
    id = request.GET['id']
    result = dm_employeedependents.listEmployeedependents(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['DELETE'])
def delEmployeedependents(request):
    id = request.GET['id']

    dm_employeedependents = dmemployeedependents()

    result = dm_employeedependents.deleteEmployeedependents(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


api_view(['GET'])
def geteditdata(request):

    id = request.GET['id']

    dm_employeedependents = dmemployeedependents()

    result = dm_employeedependents.getEmployeedependentsEditData(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['POST'])
def updateemployeedependents(request):
    id = request.data['id']
    dep_Name = request.data['depName']
    dep_Relation = request.data['depRelation']
    dep_dob = request.data['depdob']
    updated_by = request.session['empId']
    updated_date = datetime.now(tz=timezone.utc)

    dm_employeedependents = dmemployeedependents()
    result = dm_employeedependents.updateEmployeedependents(id,dep_Name,dep_Relation,dep_dob,updated_by,updated_date)
    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)