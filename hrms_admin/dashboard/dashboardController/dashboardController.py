import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
import time
from hrms_admin.dashboard.dashboardService.dashboardService import getcount


@api_view(['GET'])
def fetchDashboardValues(request):
    get_count = getcount()

    result = get_count.getcountdata()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['POST'])
def managerProjectCount(request):
    id = request.data['id']

    get_count = getcount()

    result = get_count.getmanagerprojectcountdata(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['POST'])
def listProjectManagerEmpAssigned(request):
    id = request.data['id']

    get_count = getcount()

    result = get_count.getProjectManagerEmpAssigned(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def getexpiringpolist(request):

    get_count = getcount()

    result = get_count.get_expiringpolist()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def getmanagerpodata(request):

    id = request.GET['id']

    get_count = getcount()

    result = get_count.getmanagerpodata(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def getmanagerexpoodata(request):

    id = request.GET['id']

    get_count = getcount()

    result = get_count.getmanagerexpoodata(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


@api_view(['GET'])
def getempresignation(request):

    id = request.GET['id']

    get_count = getcount()

    result = get_count.getemployeeresignations(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)



@api_view(['GET'])
def ListEmployeeResignations(request):

    id = request.GET['id']

    get_count = getcount()

    result = get_count.listEmployeeresignations(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)



@api_view(['GET'])
def geteditdata(request):
    id = request.GET['id']
    get_count = getcount()
    result = get_count.geteditdata(id)
    dataobj = {'data': result}
    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)
