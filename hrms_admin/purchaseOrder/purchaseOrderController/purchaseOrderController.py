import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder

from datetime import datetime
from django.utils import timezone


from hrms_admin.purchaseOrder.purchaseOrderService.purchaseOrderService import purchaseOrder


@api_view(['POST'])
def savePurchaseOrder(request):
    projectName = request.data['projectName']
    purchaseOrderNumber = request.data['purchaseOrderNumber']
    startDate = request.data['startDate']
    endDate = request.data['endDate']
    # purchaseOrderResources = request.data['purchaseOrderResources']
    # billingType = request.data['billingType']
    purchaseOrderAmount = request.data['purchaseOrderAmount']
    purchaseordercurrency = request.data['purchaseordercurrency']
    # projBillRate = request.data['projBillRate']
    # projectCost = request.data['projectCost']
    createdby = request.session['empId']
    createdDate = datetime.now(tz=timezone.utc)
    purchase_order = purchaseOrder()
    result = purchase_order.savePo(projectName,purchaseOrderNumber,startDate,endDate,purchaseOrderAmount,purchaseordercurrency,createdby,createdDate)

    dataobj = {'data':result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)


@api_view(['GET'])
def listPo(request):
    purchase_order = purchaseOrder()
    result = purchase_order.listpo()
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)

@api_view(['DELETE'])
def delPoData(request):
    id = request.GET['id']
    purchase_order = purchaseOrder()
    result = purchase_order.delpo(id)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)

@api_view(['GET'])
def getpoEditData(request):
    id = request.GET['id']
    purchase_order = purchaseOrder()
    result = purchase_order.getEditData(id)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)

@api_view(['POST'])
def updatepo(request):
    id = request.data['id']
    projectId = request.data['projectId']
    poNumber = request.data['poNumber']
    startDate = request.data['startDate']
    endDate = request.data['endDate']
    poAmount = request.data['poAmount']
    currencyId = request.data['currencyId']
    updated_by = request.session['empId']
    updated_date = datetime.now(tz=timezone.utc)
    purchase_order = purchaseOrder()
    result = purchase_order.updatePo(id,projectId,poNumber,startDate,endDate,poAmount,currencyId,updated_by,updated_date)
    dataobj = {'data':result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)


@api_view(['POST'])

def SavePoPayment(request):
    id=request.data['id']
    CheckTransactionDetails=request.data['CheckTransactionDetails']
    receiveddate=request.data['receiveddate']
    Description=request.data['Description']
    createdby = request.session['empId']
    createdDate = datetime.now(tz=timezone.utc)
    purchase_order = purchaseOrder()
    result = purchase_order.savepopayment(id,CheckTransactionDetails,receiveddate,Description,createdby,createdDate)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)

def getpaymentdetails(request):
    purchase_order = purchaseOrder()
    result=purchase_order.getpopayment()
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)









