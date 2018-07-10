import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from hrms_employee.employee.employeeservice.employeeservice import dmemployee
from datetime import datetime
from django.utils import timezone



@api_view(['POST'])
def saveEmployee(request):
    firstName = request.data['empFirstName']
    middleName = request.data.get('empMiddleName')
    lastName = request.data['empLastName']
    email = request.data['empEmail']
    personalemail = request.data['empPersonalEmail']
    empmobnum = request.data['empMobNum']
    empdob = request.data['empDob']
    empstatus = request.data['status']
    empjobtitle = request.data['jobTitle']
    empDoj = request.data['doj']
    empofficeno = request.data.get('officeNumber')
    empisactive= '1'
    empexperience= request.data['experience']
    empbusinessunit = request.data['businessUnit']
    empmanager = request.data.get('manager')
    empofficelocation = request.data['officeLocation']
    empcurrentaddr = request.data['empCurrAddr']
    empperaddr = request.data['empPermaAddr']
    dmempid = request.data['dmEmpID']
    myfile = request.FILES['file']
    empRole = request.data['empRole']
    created_by = request.session['empId']
    created_date = datetime.now(tz=timezone.utc)

    dm_employee = dmemployee()

    result = dm_employee.saveEmployee(firstName, middleName,lastName, email, personalemail, empmobnum,
                                      empdob, empstatus, empjobtitle, empDoj, empofficeno, empisactive,
                                      empexperience, empbusinessunit, empofficelocation, empcurrentaddr,
                                      empperaddr, empmanager,dmempid, myfile, empRole,created_date,created_by)


    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def listEmployee(request):
    dm_employee = dmemployee()

    result = dm_employee.listEmployee()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['DELETE'])
def delEmployee(request):
    id = request.GET['id']

    dm_employee = dmemployee()

    result = dm_employee.delEmployee(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def geteditdata(request):
    id = request.GET['id']
    dm_employee = dmemployee()

    result = dm_employee.geteditEmployeedata(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['POST'])
def updateEmployee(request):
    id = request.data['id']
    empFirstName = request.data['empFirstName']
    empMiddleName = request.data.get('empMiddleName')
    empLastName = request.data['empLastName']
    empEmail = request.data['empEmail']
    empPersonalEmail = request.data['empPersonalEmail']
    empMobNum = request.data['empMobNum']
    empDob = request.data['empDob']
    status = request.data['status']
    jobTitle = request.data['jobTitle']
    doj = request.data['doj']
    dol = request.data.get('dol')
    officeNumber = request.data['officeNumber']
    isActive = request.data['isActive']
    experience = request.data['experience']
    businessUnit = request.data['businessUnit']
    manager = request.data['manager']
    officeLocation = request.data['officeLocation']
    empCurrAddr = request.data['empCurrAddr']
    empPermaAddr = request.data['empPermaAddr']
    myfile = ''
    empRole = request.data['empRole']
    if request.FILES.get('file', False):
        myfile = request.FILES['file']

    updated_by = request.session['empId']
    updated_date = datetime.now(tz=timezone.utc)

    dm_employee = dmemployee()

    result = dm_employee.updateEmployee(id, empFirstName, empMiddleName, empLastName, empEmail,
                                        empPersonalEmail, empMobNum, empDob, status, jobTitle,
                                        doj, dol, officeNumber, isActive, experience, businessUnit,
                                        manager, officeLocation, empCurrAddr, empPermaAddr, myfile,empRole,updated_date,updated_by)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['POST'])
def advancesearch(request):
    columnName = request.data['column_name']
    searchText = request.data['search_text']
    dbCondition = request.data['db_condition']
    dm_employee = dmemployee()

    result = dm_employee.advanceSearch(columnName, searchText, dbCondition)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

# get add page data controller
@api_view(['GET'])
def employeedesignation(request):
    dm_employee = dmemployee()

    result = dm_employee.employeedesignationvalues()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def employeebusinessunit(request):
    dm_employee = dmemployee()

    result = dm_employee.employeebusinessunitvalues()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def employeeofficelocation(request):
    dm_employee = dmemployee()

    result = dm_employee.employeeofficelocationvalues()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def employeeManager(request):
    name = request.GET['name']
    dm_employee = dmemployee()

    result = dm_employee.empManagerName(name)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)



@api_view(['GET'])
def getEmp360Details(request):

    id = request.GET['id']

    dm_employee = dmemployee()

    result = dm_employee.getEmp360Details(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def getEmp360IncrementDetails(request):

    id = request.GET['id']

    dm_employee = dmemployee()

    result = dm_employee.getEmp360IncrementDetails(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def getEmp360EducationDetails(request):

    id = request.GET['id']

    dm_employee = dmemployee()

    result = dm_employee.getEmp360EducationDetails(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)



