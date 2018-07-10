import json
from rest_framework.decorators import api_view
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder
from hrms_employee.empdesigpackhistory.empdesigpackhistoryService.empdesigpackhistoryService import employeeHistory
from datetime import datetime
from django.utils import timezone

@api_view(['GET'])
def employeefullname(request):
    employee_history = employeeHistory()

    result=employee_history.getEmployeeName()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def currency(request):
    employee_history = employeeHistory()

    result=employee_history.getcurrency()

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['POST'])
def saveEmpDesigPackHistory(request):
    emp_id = request.data['emp_id']
    salary = request.data['salary']
    from_date = request.data['from_date']
    active = request.data['active']
    currency_id = request.data['currency_id']
    designation_id = request.data['designation_id']
    created_by = request.session['empId']
    created_date = datetime.now(tz=timezone.utc)

    employee_history = employeeHistory()

    result = employee_history.saveEmployeeDesignPackHistory(emp_id,salary,from_date,active,currency_id,designation_id,created_date, created_by)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['GET'])
def listEmpDesigPackHistory(request):

    id = request.GET['id']

    employee_history = employeeHistory()

    result = employee_history.listingEmployeeDesignPackHistory(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['POST'])
def delEmpDesigPackHistory(request):
    id = request.GET['id']

    employee_history = employeeHistory()

    result = employee_history.deleteEmployeeDesignPackHistory(id)

    dataobj = {'editdata': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

api_view(['GET'])
def getEmpDesigPackHistoryEditData(request):
    id = request.GET['id']

    employee_history = employeeHistory()

    result = employee_history.EmployeeDesignPackHistoryEditData(id)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)

@api_view(['POST'])
def updateEmpDesigPackHistory(request):
    empdesigpack_id = request.data['empdesigpack_id']
    emp_id = request.data['emp_id']
    salary = request.data['salary']
    from_date = request.data['from_date']
    active = request.data['active']
    currency_id = request.data['currency_id']
    designation_id = request.data['designation_id']
    updated_by = request.session['empId']
    updated_date = datetime.now(tz=timezone.utc)

    employee_history = employeeHistory()

    result = employee_history.updateEmployeeDesignPackHistory(empdesigpack_id,emp_id, salary, from_date, active, currency_id,
                                                            designation_id, updated_date, updated_by)

    dataobj = {'data': result}

    return HttpResponse(json.dumps(dataobj, cls=DjangoJSONEncoder), content_type='application/json', status=200)


