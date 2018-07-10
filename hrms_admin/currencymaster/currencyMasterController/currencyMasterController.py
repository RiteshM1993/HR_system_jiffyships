import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from hrms_admin.currencymaster.currencyMasterService.currencyMasterService import currencyMaster
from datetime import datetime
from django.utils import timezone


@api_view(['POST'])
def addCurrency(request):
    currencyname = request.data['currencyName']
    currencylogo = request.data['currencyLogo']
    created_by = request.session['empId']
    created_date = datetime.now(tz=timezone.utc)

    currency_master = currencyMaster()

    result = currency_master.addCurrency(currencyname, currencylogo, created_date, created_by)

    dataobj = {'data':result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def listCurrency(request):
    currency_master = currencyMaster()

    result = currency_master.listCurrency()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['DELETE'])
def delCurrency(request):
    id = request.GET['id']

    currency_master = currencyMaster()

    result = currency_master.deleteCurrency(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def geteditdata(request):

    id = request.GET['id']

    currency_master = currencyMaster()

    result = currency_master.getCurrencyEditData(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['POST'])
def updatecurrency(request):
    id = request.data['id']
    currencyname = request.data['currencyName']
    currencylogo = request.data['currencyLogo']
    updated_by = request.session['empId']
    updated_date = datetime.now(tz=timezone.utc)

    currency_master = currencyMaster()

    result = currency_master.updateCurrency(id, currencyname, currencylogo, updated_by,updated_date)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

