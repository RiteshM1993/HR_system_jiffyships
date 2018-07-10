import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from hrms_employee.empexperience.empExperienceService.empExperienceService import employeeExperience
from datetime import datetime
from django.utils import timezone


@api_view(['POST'])
def saveEmpExperience(request):
    data = request.data['data']
    empId = request.session['empId']
    created_by = request.session['empId']
    created_date = datetime.now(tz=timezone.utc)

    emp_experience = employeeExperience()

    result = emp_experience.saveEmployeeExperience(data,empId,created_by,created_date)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def listEmpExperience(request):
    id = request.GET['id']

    emp_experience = employeeExperience()

    result = emp_experience.listingEmployeeExperience(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)
@api_view(['DELETE'])
def delEmpExperience(request):
    id = request.GET['id']
    emp_experience = employeeExperience()

    result = emp_experience.deleteEmployeeExperience(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['POST'])
def getEditDataEmpExperience(request):
    id = request.data['id']

    emp_experience = employeeExperience()

    result = emp_experience.geteditEmployeeExperiencedata(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)
@api_view(['POST'])
def updateEmpExperience(request):
    id = request.data['id']
    prevCompanyName = request.data['prevCompanyName']
    jobTitle = request.data['jobTitle']
    fromDate = request.data['fromDate']
    toDate = request.data['toDate']
    jobDescription = request.data['jobDescription']
    empId = request.session['empId']
    updated_by = request.session['empId']
    updated_date = datetime.now(tz=timezone.utc)

    emp_experience = employeeExperience()

    result = emp_experience.updateEmployeeExperience(id,prevCompanyName,jobTitle,fromDate,toDate,jobDescription, empId, updated_by,updated_date)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


