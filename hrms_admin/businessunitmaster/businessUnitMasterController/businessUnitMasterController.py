import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from hrms_admin.businessunitmaster.businessUnitMasterService.businessUnitMasterService import businessUnitMaster
from datetime import datetime
from django.utils import timezone

@api_view(['POST'])
def addbusinessunit(request):
    business_name = request.data['businessUnitName']
    business_parent = request.data.get('businessParent')
    status = request.data['status']
    managerId = request.data['managerId']
    created_by = request.session['empId']
    created_date = datetime.now(tz=timezone.utc)

    business_unit_master = businessUnitMaster()
    result = business_unit_master.addBusinessUnitMaster(business_name, business_parent, status,managerId,created_by,created_date)
    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def lisbusinessunit(request):
    business_unit_master = businessUnitMaster()
    result = business_unit_master.listBusinessUnitMaster()
    dataobj = {'data': result }

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['DELETE'])
def delbusinessunit(request):
    id = request.GET['id']
    business_unit_master = businessUnitMaster()
    result = business_unit_master.delBusinessUnitMaster(id)
    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def geteditdata(request):
    id = request.GET['id']
    business_unit_master = businessUnitMaster()
    result = business_unit_master.geteditdata(id)
    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['POST'])
def updatebusinessunit(request):
    id = request.data['id']
    business_name = request.data['businessUnitName']
    business_parent = request.data['businessParent']
    status = request.data['status']
    managerId = request.data['manager_id']
    updated_by = request.session['empId']
    updated_date = datetime.now(tz=timezone.utc)

    business_unit_master = businessUnitMaster()
    result = business_unit_master.updateBusinessUnitMaster(id,business_name, business_parent, status,managerId, updated_by, updated_date)
    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)