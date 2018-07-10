import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from hrms_employee.employeeeducation.employeeeducationservice.employeeeducationservice import dmemployeeeducation
from datetime import datetime
from django.utils import timezone


@api_view(['POST'])
def saveempEdugrid(request):
    Data=request.data['data']
    empid = request.session['empId']
    created_by = request.session['empId']
    created_date = datetime.now(tz=timezone.utc)

    dm_employeeeducation = dmemployeeeducation()
    result = dm_employeeeducation.saveempEdugrid(Data,empid,created_by,created_date)
    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def listEmployeeeducation(request):

    id=request.GET['id']
    dm_employeeeducation = dmemployeeeducation()

    result = dm_employeeeducation.listEmployeeeducation(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['DELETE'])
def deleteEmployeeeducation(request):
    id = request.GET['id']

    dm_employeeeducation = dmemployeeeducation()

    result = dm_employeeeducation.deleteemployeeducation(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def geteditdata(request):

    id = request.GET['id']

    dm_employeeeducation = dmemployeeeducation()

    result = dm_employeeeducation.getEmployeeeducationEditData(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['POST'])
def updateemployeeEducation(request):
    id = request.data['id']
    empSchoolUniv_Name = request.data['schUnivName']
    empQuali_Degr_Name = request.data['quaDegname']
    empDoc = request.data['Doc']
    empNotes = request.data['Notes']
    updated_by = request.session['empId']
    updated_date = datetime.now(tz=timezone.utc)

    dm_employeeeducation = dmemployeeeducation()
    result = dm_employeeeducation.updateemployeeEducation(id,empSchoolUniv_Name,empQuali_Degr_Name,empDoc,empNotes,updated_by,updated_date)
    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


