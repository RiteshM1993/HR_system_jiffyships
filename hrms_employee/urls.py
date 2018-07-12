from django.conf.urls import url
from hrms_employee import views
from hrms_employee.employee.employeecontroller import employeecontroller
from hrms_employee.empdesigpackhistory.empdesigpackhistoryController import empdesigpackhistoryController
from hrms_employee.empexperience.empExperienceController import empExperienceController
from hrms_employee.emptype.empTypeController import empTypeController

from hrms_employee.employeedependents.employeedependentscontroller import employeedependentscontroller
from hrms_employee.employeeeducation.employeeeducationcontroller import employeeeducationcontroller
from hrms_employee.employeeproject.employeeprojectcontroller import employeeprojectcontroller
from hrms_employee.uploadempdoc.uploadempdoccontroller import uploadempdoccontroller
from hrms_employee.empresign.empresignController import empresignController



urlpatterns =[

    # view
    url(r'^employee/$', views.employeeDashboardView.as_view()),

    # employee

    url(r'^employee/api/saveemployee/$', employeecontroller.saveEmployee),
    url(r'^employee/api/listemployee/$', employeecontroller.listEmployee),
    url(r'^employee/api/delemployee/$', employeecontroller.delEmployee),
    url(r'^employee/api/geteditemployeedata/$', employeecontroller.geteditdata),
    url(r'^employee/api/updateemployee/$', employeecontroller.updateEmployee),
    url(r'^employee/api/advancesearch/$', employeecontroller.advancesearch),
        # get values for save page
    url(r'^employee/api/employeedesignationvalues/$', employeecontroller.employeedesignation),
    url(r'^employee/api/employeebusinessunitvalues/$', employeecontroller.employeebusinessunit),
    url(r'^employee/api/employeeofficelocationvalue/$', employeecontroller.employeeofficelocation),
    url(r'^employee/api/listmanagerename/$', employeecontroller.employeeManager),


    # employee designation package history

    url(r'^employee/api/saveemp_desig_pack_history/$', empdesigpackhistoryController.saveEmpDesigPackHistory),
    url(r'^employee/api/listempdesigpackhistory/$', empdesigpackhistoryController.listEmpDesigPackHistory),
    url(r'^employee/api/delempdesigpackhistory/$', empdesigpackhistoryController.delEmpDesigPackHistory),
    url(r'^employee/api/getempdesigpackhistoryeditdata/$', empdesigpackhistoryController.getEmpDesigPackHistoryEditData),
    url(r'^employee/api/updateempdesigpackhistory/$', empdesigpackhistoryController.updateEmpDesigPackHistory),

        # get values for save page
        url(r'^employee/api/getempname/$', empdesigpackhistoryController.employeefullname),
        url(r'^employee/api/getcurrency/$', empdesigpackhistoryController.currency),

    # employee Experience
    url(r'^employee/api/saveEmpExperience/$', empExperienceController.saveEmpExperience),
    url(r'^employee/api/listempexperience/$', empExperienceController.listEmpExperience),
    url(r'^employee/api/delempexperience/$', empExperienceController.delEmpExperience),
    url(r'^employee/api/geteditEmpExperiencedata/$', empExperienceController.getEditDataEmpExperience),
    url(r'^employee/api/updateEmpExperiencedata/$', empExperienceController.updateEmpExperience),

    # employee type
    url(r'^employee/api/saveemptype/$', empTypeController.saveEmpType),
    url(r'^employee/api/listemptype/$', empTypeController.listEmpType),
    url(r'^employee/api/delemptype/$', empTypeController.deleteEmpType),
    url(r'^employee/api/getemptype/$', empTypeController.getdataEmpType),
    url(r'^employee/api/updateemptype/$', empTypeController.updateEmpType),

    # Ritesh

    #employeedependents
    url(r'^employee/api/saveemployeedependents/$', employeedependentscontroller.saveEmployeedependents),
    url(r'^employee/api/listemployeedependents/$', employeedependentscontroller.listEmployeedependents),
    url(r'^employee/api/deleteemployeedependents/$', employeedependentscontroller.delEmployeedependents),
    url(r'^employee/api/geteditemployeedependentsdata/$', employeedependentscontroller.geteditdata),
    url(r'^employee/api/updateemployeedependents/$', employeedependentscontroller.updateemployeedependents),

    #employeeeducation
    url(r'^employee/api/saveEmpEducation/$', employeeeducationcontroller.saveempEdugrid),
    url(r'^employee/api/listemployeeeducation/$', employeeeducationcontroller.listEmployeeeducation),
    url(r'^employee/api/deleteemployeeducation/$', employeeeducationcontroller.deleteEmployeeeducation),
    url(r'^employee/api/geteditemployeeeducationdata/$', employeeeducationcontroller.geteditdata),
    url(r'^employee/api/updateemployeeeducation/$', employeeeducationcontroller.updateemployeeEducation),

    # employeeproject

    url(r'^employee/api/saveemployeeproject/$', employeeprojectcontroller.saveEmployeeprojecttype),
    url(r'^employee/api/listEmployeeproject/$', employeeprojectcontroller.listEmployeeproject),
    url(r'^employee/api/deleteemployeeproject/$', employeeprojectcontroller.deleteEmployeeproject),
    url(r'^employee/api/geteditemployeeproject/$', employeeprojectcontroller.geteditdata),
    url(r'^employee/api/updateemployeeproject/$', employeeprojectcontroller.updateEmployeeproject),
    url(r'^employee/api/getstartenddate/$', employeeprojectcontroller.getStartEndDate),



    # get values for save page
    url(r'^employee/api/employeenamevalues/$', employeeprojectcontroller.employeename),
    url(r'^employee/api/projecttypemastervalue/$', employeeprojectcontroller.projecttype),

    #resource Count and data
    url(r'^dashboard/api/getresources/$', employeeprojectcontroller.getResources),
    url(r'^dashboard/api/getdocuments/$', employeeprojectcontroller.getDocuments),


    # emp doc
    url(r'^employee/api/saveempdoc/$', uploadempdoccontroller.saveEmpDoc),
    url(r'^employee/api/listempdoc/$', uploadempdoccontroller.listEmpDoc),
    url(r'^employee/api/delempdoc/$', uploadempdoccontroller.deleteEmpDoc),
    url(r'^employee/api/geteditempdoc/$', uploadempdoccontroller.getEditEmpdoc),
    url(r'^employee/api/updateempdoc/$', uploadempdoccontroller.updateEmpdoc),


#   emp resign
    url(r'^employee/api/saveemployeeresign/$', empresignController.saveEmpResign),
    url(r'^employee/api/listEmployeeresignation/$', empresignController.listEmpResign),
    url(r'^employee/api/myresignation/$', empresignController.getEmpeResignData),
    url(r'^employee/api/editemployeeresignations/$', empresignController.geteditdata),
    # url(r'^employee/api/updateemployeeresignation/$', empresignController.updateEmpeResignData),

    #   employee timeline
    url(r'^employee/api/getEmp360Details/$', employeecontroller.getEmp360Details),
    url(r'^employee/api/getEmp360IncrementDetails/$', employeecontroller.getEmp360IncrementDetails),
    url(r'^employee/api/getEmp360EducationDetails/$', employeecontroller.getEmp360EducationDetails),








]