from django.conf.urls import url
from businessunitmaster.businessUnitMasterController import businessUnitMasterController
from currencymaster.currencyMasterController import currencyMasterController
from officelocation.officeLocationController import officeLocationController
from hrms_admin.designationmaster.designationmastercontroller import designationmastercontroller
from hrms_admin.projecttypemaster.projecttypemastercontroller import projecttypemastercontroller
from hrms_admin.dashboard.dashboardController import dashboardController
from hrms_admin.projectmaster.projectmastercontroller import projectmastercontroller

from hrms_admin.login.logincontroller import logincontroller
from hrms_admin.projectdocu.projectDocuController import  projectDocuController

from hrms_admin.billing.billingController import billingController
from hrms_admin.customermaster.customermastercontroller import customermastercontroller

from hrms_admin.purchaseOrder.purchaseOrderController import purchaseOrderController

from hrms_employee.empresign.empresignController import empresignController

urlpatterns =[

    # business unit master
    url('^dashboard/api/savebusinessunit/$', businessUnitMasterController.addbusinessunit),
    url('^dashboard/api/listbusinessunit/$', businessUnitMasterController.lisbusinessunit),
    url('^dashboard/api/delbusinessunit/$', businessUnitMasterController.delbusinessunit),
    url('^dashboard/api/geteditdata/$', businessUnitMasterController.geteditdata),
    url('^dashboard/api/updatebusinessunit/$', businessUnitMasterController.updatebusinessunit),

    # currency Master

    url('^dashboard/api/addcurrency/$', currencyMasterController.addCurrency),
    url('^dashboard/api/listcurrency/$', currencyMasterController.listCurrency),
    url('^dashboard/api/delcurrency/$', currencyMasterController.delCurrency),
    url('^dashboard/api/geteditcurrencydata/$', currencyMasterController.geteditdata),
    url('^dashboard/api/updatecurrency/$', currencyMasterController.updatecurrency),

    # office location

    url('^dashboard/api/saveofficelocation/$', officeLocationController.saveOfficeLocation),
    url('^dashboard/api/listofficelocations/$', officeLocationController.listOfficeLocation),
    url('^dashboard/api/delofficelocations/$', officeLocationController.delOfficeLocation),
    url('^dashboard/api/geteditofficelocations/$', officeLocationController.geteditofficelocations),
    url('^dashboard/api/updateofficelocation/$', officeLocationController.updateofficelocations),


    # Designation

    url('^dashboard/api/savedesignation/$', designationmastercontroller.saveDesignation),
    url('^dashboard/api/listdesignation/$', designationmastercontroller.listDesignation),
    url('^dashboard/api/deletedesignation/$', designationmastercontroller.deleteDesignation),
    url('^dashboard/api/geteditdesignationdata/$', designationmastercontroller.geteditdata),
    url('^dashboard/api/updatedesignation/$', designationmastercontroller.updateDesignation),

    #Project Type

    url('^dashboard/api/saveprojecttype/$', projecttypemastercontroller.saveProjecttype),
    url('^dashboard/api/listprojecttype/$', projecttypemastercontroller.listProjecttype),
    url('^dashboard/api/deleteprojecttype/$', projecttypemastercontroller.deleteProjecttype),
    url('^dashboard/api/geteditprojecttypedata/$', projecttypemastercontroller.geteditdata),
    url('^dashboard/api/getupdateprojecttype/$', projecttypemastercontroller.updateProjecttype),

    #Dashboard
    url('^dashboard/api/fetchdashboardvalues/$', dashboardController.fetchDashboardValues),
    url('^dashboard/api/managerprojectcount/$', dashboardController.managerProjectCount),
    url('^dashboard/api/listprojectmanagerempassigned/$', dashboardController.listProjectManagerEmpAssigned),
    url('^dashboard/api/getexpiringpolist/$', dashboardController.getexpiringpolist),
    url('^dashboard/api/getmanagerpodata/$', dashboardController.getmanagerpodata),
    url('^dashboard/api/getmanagerexpoodata/$', dashboardController.getmanagerexpoodata),
    url('^dashboard/api/ListEmployeeResignations/$', dashboardController.ListEmployeeResignations),


    url(r'^dashboard/api/editemployeeresignations/$', empresignController.geteditdata),
    url(r'^dashboard/api/updateemployeeresignation/$', empresignController.updateEmpeResignData),

    # project Master

    url('^dashboard/api/saveprojectmaster/$', projectmastercontroller.saveProjectMaster),
    url('^dashboard/api/listprojectmaster/$', projectmastercontroller.listprojectmaster),
    url('^dashboard/api/deleteeprojectmaster/$', projectmastercontroller.deleteprojectmaster),
    url('^dashboard/api/geteditprojectmaster/$', projectmastercontroller.geteditdata),
    url('^dashboard/api/updateeprojectmaster/', projectmastercontroller.updateprojectmaster),
    url('^dashboard/api/customervalues/$', projectmastercontroller.customervalues),
    url('^dashboard/api/getprojectpo/$', projectmastercontroller.getprojectpo),
    url('^dashboard/api/getcustomerproject/$', projectmastercontroller.getcustomerproject),
    url('^dashboard/api/getcustomerprojectpo/$', projectmastercontroller.getcustomerprojectpo),


    url('^dashboard/api/projectbusinessunitvalues/$', projectmastercontroller.employeebusinessunit),
    url('^dashboard/api/projectmastervalues/$', projectmastercontroller.projecttype),
    url('^dashboard/api/managernamevalues/$', projectmastercontroller.employeename),

    # Session login logout
    url('^api/userlogin/$', logincontroller.login),
    url('^dashboard/api/checksession/$', logincontroller.checksession),
    url('^dashboard/api/signout/$', logincontroller.logout),


    # project doc

    url('^dashboard/api/saveprodoc/$', projectDocuController.saveProjDoc),
    url('^dashboard/api/projectnamevalues/$', projectDocuController.projectnamevalues),
    url('^dashboard/api/listprojectdocument/$', projectDocuController.listProjDoc),
    url('^dashboard/api/delProjDoc/$', projectDocuController.deleteProjDoc),
    url('^dashboard/api/getEditProjdoc/$', projectDocuController.getEditProjdoc),
    url('^dashboard/api/updateProjDoc/$', projectDocuController.updateProjdoc),


    #billing
    url('^dashboard/api/ProjectNameValues/$', billingController.ProjectNameValues),
    url('^dashboard/api/savebilling/$', billingController.savebilling),
    url('^dashboard/api/listbilling/$', billingController.listbilling),
    url('^dashboard/api/generatebilling/$', billingController.generatebilling),

    #project document

    url(r'^dashboard/api/getDocuments/$', projectmastercontroller.getDocuments),



    url('^dashboard/api/savecustomermaster/$', customermastercontroller.saveCustomerMaster),
    url('^dashboard/api/listcustomer/$', customermastercontroller.listCustomer),
    url('^dashboard/api/geteditcustomer/$', customermastercontroller.geteditdata),
    url('^dashboard/api/updatecustomer/$', customermastercontroller.updateCustomer),

    # Purchase Order
    url('^dashboard/api/savepurchaseorder/$', purchaseOrderController.savePurchaseOrder),
    url('^dashboard/api/listpo/$', purchaseOrderController.listPo),
    url('^dashboard/api/delpodata/$', purchaseOrderController.delPoData),
    url('^dashboard/api/poeditdata/$', purchaseOrderController.getpoEditData),
    url('^dashboard/api/updatepo/$', purchaseOrderController.updatepo),
    url('^dashboard/api/savepopayment/$', purchaseOrderController.SavePoPayment),
    url('^dashboard/api/getpoPayment/$', purchaseOrderController.getpaymentdetails),

]