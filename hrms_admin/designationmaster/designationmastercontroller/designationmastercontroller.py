import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from hrms_admin.designationmaster.designationmasterservice.designationmasterservice import dmdesignation
from datetime import datetime
from django.utils import timezone


@api_view(['POST'])
def saveDesignation(request):
    designationName = request.data['des_name']
    created_by = request.session['empId']
    created_date = datetime.now(tz=timezone.utc)

    dm_designation = dmdesignation()
    result = dm_designation.saveDesignation(designationName,created_by,created_date)
    dataobj ={'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def listDesignation(request):
    dm_designation = dmdesignation()
    result = dm_designation.listDesignation()
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['DELETE'])
def deleteDesignation(request):
    id = request.GET['id']
    dm_designation = dmdesignation()
    result = dm_designation.deleteDesignation(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)
@api_view(['GET'])
def geteditdata(request):
    id = request.GET['id']
    dm_designation = dmdesignation()
    result = dm_designation.geteditDesignationdata(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['POST'])
def updateDesignation(request):
    id = request.data['id']
    designationName = request.data['des_name']
    updated_by = request.session['empId']
    updated_date = datetime.now(tz=timezone.utc)

    dm_designation = dmdesignation()

    result = dm_designation.updateDesignation(id, designationName, updated_by, updated_date)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)
