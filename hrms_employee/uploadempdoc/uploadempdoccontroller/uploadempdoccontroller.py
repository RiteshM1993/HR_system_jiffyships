import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from hrms_employee.uploadempdoc.uploadempdocservice.uploadempdocservice import empDoc
from datetime import datetime
from django.utils import timezone


@api_view(['POST'])
def saveEmpDoc(request):
    doc_name = request.data['docName']
    doc_file = request.data['file']
    empid = request.session['empId']
    created_by = request.session['empId']
    created_date = datetime.now(tz=timezone.utc)

    emp_doc = empDoc()
    result = emp_doc.saveEmpDoc(doc_name,doc_file,empid,created_date,created_by)
    dataobj = {'data':result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)

@api_view(['GET'])
def listEmpDoc(request):
    emp_doc = empDoc()
    result = emp_doc.listingEmpDoc()
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)


@api_view(['DELETE'])
def deleteEmpDoc(request):
    id = request.GET['id']
    emp_doc = empDoc()
    result = emp_doc.deleteEmpDoc(id)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)


@api_view(['GET'])
def getEditEmpdoc(request):
    id = request.GET['id']
    emp_doc = empDoc()
    result = emp_doc.getEmpeditDocdata(id)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)


@api_view(['POST'])
def updateEmpdoc(request):
    id = request.data['id']
    docName = request.data['docName']
    doc_file = request.data['file']
    updated_by = request.session['empId']
    updated_date = datetime.now(tz=timezone.utc)

    emp_doc = empDoc()
    result = emp_doc.updateEmpdoc(id,docName,doc_file,updated_by,updated_date)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)




