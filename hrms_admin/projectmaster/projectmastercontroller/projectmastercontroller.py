import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from hrms_admin.projectmaster.projectmasterservice.projectmasterservice import dmprojectmaster
from datetime import datetime
from django.utils import timezone


@api_view(['POST'])
def saveProjectMaster(request):
    customerId=request.data['customerId']
    projectName = request.data['projectName']
    projecttypeMasterid = request.data.get('projecttypeMasterid')
    startDate = request.data['startDate']
    endDate = request.data['endDate']
    resourceCount = request.data['resourceCount']
    businessUNitid = request.data['businessUNitid']
    emp_id=request.data['emp_id']
    # projcurr=request.data['projcurr']
    # projBillRate=request.data['projBillRate']
    projectCost=request.data['projectCost']
    created_by = request.session['empId']
    created_date = datetime.now(tz=timezone.utc)

    dm_projectmaster = dmprojectmaster()

    result = dm_projectmaster.saveProjectMaster(projectName,projecttypeMasterid,startDate,endDate,resourceCount,businessUNitid,emp_id,customerId,projectCost,created_by,created_date)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def employeename(request):
    name=request.GET['name']

    dm_projectmaster = dmprojectmaster()

    result = dm_projectmaster.listemployeevalues(name)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)



@api_view(['GET'])
def listprojectmaster(request):
    dm_projectmaster = dmprojectmaster()

    result = dm_projectmaster.listprojectMaster()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['DELETE'])
def deleteprojectmaster(request):
    id = request.GET['id']

    dm_projectmaster = dmprojectmaster()

    result = dm_projectmaster.deleteprojectmaster(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def geteditdata(request):

    id = request.GET['id']

    dm_projectmaster = dmprojectmaster()

    result = dm_projectmaster.getprojectmasterdata(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['POST'])
def updateprojectmaster(request):
    id = request.data['id']
    projectName = request.data['projectName']
    projecttypeMasterid = request.data['projecttypeMasterid']
    start_date = request.data['start_date']
    end_date = request.data['end_date']
    resourceCount=request.data['resourceCount']
    businessUNitid=request.data['businessUNitid']
    emp_id = request.data['emp_id']
    # currency_name = request.data['currency_name']
    # rate_per_hour = request.data['rate_per_hour']
    projectCost = request.data['projectCost']
    customer_id = request.data['customer_id']
    updated_by = request.session['empId']
    updated_date = datetime.now(tz=timezone.utc)

    dm_projectmaster = dmprojectmaster()

    result = dm_projectmaster.updateeprojectmaster(id,projectName, projecttypeMasterid,start_date,end_date,resourceCount,businessUNitid,emp_id,customer_id,projectCost, updated_by, updated_date)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def employeebusinessunit(request):
    dm_projectmaster = dmprojectmaster()

    result = dm_projectmaster.employeebusinessunitvalues()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def projecttype(request):
    dm_projectmaster = dmprojectmaster()

    result = dm_projectmaster.projecttypevalues()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def getDocuments(request):
    id = request.GET['id']
    dm_projectmaster = dmprojectmaster()

    result = dm_projectmaster.getProjectDocument(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)




@api_view(['GET'])
def customervalues(request):
    dm_projectmaster = dmprojectmaster()

    result = dm_projectmaster.getcustomervalues()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def getprojectpo(request):
    id = request.GET['id']
    dm_projectmaster = dmprojectmaster()

    result = dm_projectmaster.getprojectpo(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def getcustomerproject(request):
    id = request.GET['id']
    dm_projectmaster = dmprojectmaster()

    result = dm_projectmaster.getcustomerproject(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def getcustomerprojectpo(request):
    id = request.GET['id']
    dm_projectmaster = dmprojectmaster()

    result = dm_projectmaster.getprojectpo(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


