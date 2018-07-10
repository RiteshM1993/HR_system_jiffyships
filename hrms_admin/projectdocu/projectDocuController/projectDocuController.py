import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from hrms_admin.projectdocu.projectDocuService.projectDocuService import projDoc
from datetime import datetime
from django.utils import timezone


@api_view(['POST'])
def saveProjDoc(request):
    project_id = request.data['project_id']
    doc_name = request.data['docName']
    doc_file = request.data['docfile']
    createdby = request.session['empId']
    createdDate = datetime.now(tz=timezone.utc)
    proj_Doc = projDoc()
    result = proj_Doc.saveProjDoc(project_id,doc_name,doc_file,createdby,createdDate)
    dataobj = {'data':result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)


@api_view(['GET'])
def projectnamevalues(request):

    proj_Doc = projDoc()

    result = proj_Doc.projectnamevalues()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)




@api_view(['GET'])
def listProjDoc(request):
    proj_Doc = projDoc()
    result = proj_Doc.listProjDoc()
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)



@api_view(['DELETE'])
def deleteProjDoc(request):
    id = request.GET['id']
    proj_Doc = projDoc()
    result = proj_Doc.deleteProjDoc(id)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)


@api_view(['GET'])
def getEditProjdoc(request):
    id = request.GET['id']
    proj_Doc = projDoc()
    result = proj_Doc.getEditProjdoc(id)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)


@api_view(['POST'])
def updateProjdoc(request):
    id = request.data['id']
    project_id = request.data['project_name']
    doc_name = request.data['docName']
    doc_file = request.data['file']
    updated_by = request.session['empId']
    updated_date = datetime.now(tz=timezone.utc)

    proj_Doc = projDoc()
    result = proj_Doc.updateProjdoc(id,project_id,doc_name,doc_file,updated_by,updated_date)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='Application/json', status=200)
