import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from hrms_admin.billing.billingService.billingService import Billing
import time
from datetime import datetime
from django.utils import timezone
from django.core import serializers



@api_view(['GET'])
def ProjectNameValues(request):
    Bill_ing = Billing()
    result = Bill_ing.projectnamevalues()
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)




@api_view(['POST'])
def savebilling(request):
    project_id = request.data['project_id']
    startDate = request.data['startDate']
    endDate = request.data['endDate']
    billresourceCount = request.data['billresourceCount']
    totalBill = request.data['totalBill']
    createdby = request.session['empId']
    createdDate = datetime.now(tz=timezone.utc)
    Bill_ing = Billing()
    result = Bill_ing.savebilling(project_id,startDate,endDate,billresourceCount,totalBill,createdby,createdDate)
    dataobj = {'data':result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)


@api_view(['GET'])
def listbilling(request):
    Bill_ing = Billing()
    result = Bill_ing.listbilling()
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)


@api_view(['GET'])
def generatebilling(request):
    Bill_ing = Billing()
    result = Bill_ing.generatebilling()
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)
