import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from hrms_admin.officelocation.officeLocationService.officeLocationService import officeLocation
from datetime import datetime
from django.utils import timezone


@api_view(['POST'])
def saveOfficeLocation(request):
    officelocation = request.data['officeLocation']
    address = request.data['address']
    created_by = request.session['empId']
    created_date = datetime.now(tz=timezone.utc)

    office_location = officeLocation()

    result = office_location.saveOfficeLocation(officelocation, address, created_date, created_by)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def listOfficeLocation(request):

    office_location = officeLocation()
    result = office_location.listOfficelocaltion()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def delOfficeLocation(request):
    id = request.GET['id']
    office_location = officeLocation()
    result = office_location.deleteOfficelocaltion(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def geteditofficelocations(request):
    id = request.GET['id']
    office_location = officeLocation()
    result = office_location.geteditofficelocaltion(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['POST'])
def updateofficelocations(request):
    id = request.data['id']
    officelocation = request.data['officeLocation']
    address = request.data['address']
    updated_by = request.session['empId']
    updated_date = datetime.now(tz=timezone.utc)

    office_location = officeLocation()

    result = office_location.updateOfficeLocation(id,officelocation, address, updated_by,updated_date)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)