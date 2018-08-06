from django.conf.urls import url
from hrms_employee import views
from hrms_employee.employee.employeecontroller import employeecontroller






urlpatterns =[

    # view
    url(r'^employee/$', views.employeeDashboardView.as_view()),

    # employee

    url(r'^employee/api/saveemployee/$', employeecontroller.saveEmployee),
    url(r'^employee/api/listemployee/$', employeecontroller.listEmployee),
    url(r'^employee/api/delemployee/$', employeecontroller.delEmployee),
    url(r'^employee/api/geteditemployeedata/$', employeecontroller.geteditdata),
    url(r'^employee/api/updateemployee/$', employeecontroller.updateEmployee),




]