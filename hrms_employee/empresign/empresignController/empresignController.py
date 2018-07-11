import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from hrms_employee.empresign.empresignService.empresignService import employeeResign
from datetime import datetime
from datetime import timedelta
from django.utils import timezone
# import dateutil.parser as dutils


@api_view(['POST'])
def saveEmpResign(request):
    resignReason = request.data['resignReason']
    resignDate = request.data['resignDate']
    resignDate = str(resignDate)
    date_of_leaving = datetime.strptime(resignDate, "%Y-%m-%d %H:%M:%S") + timedelta(days=90)
    emp_id = request.session['empId']
    updated_by = request.session['empId']
    updated_date = datetime.now(tz=timezone.utc)
    resign_status = 1;

    employee_resign = employeeResign()
    result = employee_resign.saveEmpResignation(resignReason,resignDate,emp_id,date_of_leaving,updated_by,updated_date,resign_status)
    dataobj = {'data':result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)

@api_view(['GET'])
def listEmpResign(request):
    employee_resign = employeeResign()
    result = employee_resign.listingEmpresign()
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)


@api_view(['DELETE'])
def deleteEmpDoc(request):
    id = request.GET['id']
    employee_resign = employeeResign()
    result = employee_resign.deleteEmpDoc(id)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)


@api_view(['GET'])
def getEmpeResignData(request):
    id = request.GET['id']
    employee_resign = employeeResign()
    result = employee_resign.getEmpeResigndata(id)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)


@api_view(['POST'])
def updateEmpdoc(request):
    id = request.data['id']
    docName = request.data['docName']
    doc_file = request.data['file']
    modifiedDate = datetime.now(tz=timezone.utc)
    employee_resign = employeeResign()
    result = employee_resign.updateEmpdoc(id,docName,doc_file,modifiedDate)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)



