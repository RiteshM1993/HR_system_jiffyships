import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from hrms_admin.projecttypemaster.projecttypemasterservice.projecttypemasterservice import dmprojecttype

from hrms_admin.customermaster.customermasterservice.customermasterservice import dmcustomermaster

from datetime import datetime
from django.utils import timezone

@api_view(['POST'])
def saveCustomerMaster(request):
    CustomerName = request.data['CustomerName']
    CustomerAddress = request.data['CustomerAddress']
    startDate = request.data['startDate']
    ContactPersonName = request.data['ContactPersonName']
    ContactPersonEmailid = request.data['ContactPersonEmailid']
    active = request.data['active']
    created_by = request.session['empId']
    created_date = datetime.now(tz=timezone.utc)

    dm_customermaster = dmcustomermaster()
    result = dm_customermaster.saveCustomer(CustomerName,CustomerAddress,startDate,ContactPersonName,ContactPersonEmailid,active, created_by, created_date)
    dataobj ={'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def listCustomer(request):
    dm_customermaster = dmcustomermaster()
    result = dm_customermaster.listcustomer()
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def geteditdata(request):
    id = request.GET['id']
    dm_customermaster = dmcustomermaster()
    result = dm_customermaster.geteditCustomer(id)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['PUT'])
def updateCustomer(request):
    id = request.data['id']
    customer_name = request.data['customer_name']
    customer_address = request.data['customer_address']
    start_date = request.data['start_date']
    contact_person_name = request.data['contact_person_name']
    contact_person_emailid = request.data['contact_person_emailid']
    status = request.data['status']
    updated_by = request.session['empId']
    updated_date = datetime.now(tz=timezone.utc)

    dm_customermaster = dmcustomermaster()

    result = dm_customermaster.updateCustomerMaster(id, customer_name,customer_address,start_date,contact_person_name,contact_person_emailid,status,updated_by,updated_date)
    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)
