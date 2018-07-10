import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from hrms_admin.projecttypemaster.projecttypemasterservice.projecttypemasterservice import dmprojecttype
from datetime import datetime
from django.utils import timezone

@api_view(['POST'])
def saveProjecttype(request):
    projecttypeName = request.data['proj_name']
    created_by = request.session['empId']
    created_date = datetime.now(tz=timezone.utc)

    dm_projecttype = dmprojecttype()
    result = dm_projecttype.saveProjecttype(projecttypeName,created_by,created_date)
    dataobj ={'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def listProjecttype(request):
    dm_projecttype = dmprojecttype()
    result = dm_projecttype.listProjecttype()
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)



@api_view(['DELETE'])
def deleteProjecttype(request):
    id = request.GET['id']
    dm_projecttype = dmprojecttype()
    result = dm_projecttype.deleteProjecttype(id)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def geteditdata(request):
    id = request.GET['id']
    dm_projecttype = dmprojecttype()
    result = dm_projecttype.geteditProjecttypedata(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['POST'])
def updateProjecttype(request):
    id = request.data['id']
    projecttypeName = request.data['proj_name']
    updated_by = request.session['empId']
    updated_date = datetime.now(tz=timezone.utc)


    dm_projecttype = dmprojecttype()

    result = dm_projecttype.updateProjecttype(id, projecttypeName, updated_by,updated_date)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)
