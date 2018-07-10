import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from hrms_employee.emptype.empTypeService.empTypeService import empType
from datetime import datetime
from django.utils import timezone


@api_view(['POST'])
def saveEmpType(request):
    empTypeName = request.data['emptypename']
    created_by = request.session['empId']
    created_date = datetime.now(tz=timezone.utc)

    emp_Type = empType()
    result = emp_Type.saveEmpType(empTypeName,created_date,created_by)
    dataobj = {'data':result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)

@api_view(['GET'])
def listEmpType(request):
    emp_Type = empType()
    result = emp_Type.listingEmpType()
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)


@api_view(['DELETE'])
def deleteEmpType(request):
    typeid = request.GET['id']
    emp_Type = empType()
    result = emp_Type.deleteEmpType(typeid)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)


@api_view(['GET'])
def getdataEmpType(request):
    typeid = request.GET['id']
    emp_Type = empType()
    result = emp_Type.getEmpTypedata(typeid)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)


@api_view(['POST'])
def updateEmpType(request):
    typeId = request.data['id']
    typeName = request.data['emptypename']
    updated_by = request.session['empId']
    updated_date = datetime.now(tz=timezone.utc)

    emp_Type = empType()
    result = emp_Type.updateEmpTypedata(typeId,typeName,updated_date,updated_by)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)




