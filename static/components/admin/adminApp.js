angular.module('adminApp',[
    'ui.router',
    'smart-table',
    'autoCompleteModule',
    'multipleSelect',
    'ngMaterial',
    'adminApp.businessUnitMaster',
    'adminApp.currencyMaster',
    'adminApp.officeLocation',
    'adminApp.designationmaster',
    'adminApp.projecttypemaster',
    'employeeApp',
    'adminApp.admindashboard',
    'adminApp.projectmaster',
    'adminApp.projectAssign',
    'adminApp.projectdocuments',
    'adminApp.billing',
    'adminApp.customermaster',
     'adminApp.purchaseOrder',
])

.config(['$stateProvider','$urlRouterProvider', function($stateProvider, $urlRouterProvider){


    $urlRouterProvider.otherwise('/admindashboard');


    $stateProvider

    .state('dashboard',{
        url: '/admindashboard',
        templateUrl: '/static/components/admin/components/dashboard/views/dashboard.html',
        controller: 'dashboardController',
        controllerAs: 'adminDashboardScope',
    })

     .state('expiringpo',{
        url:'/expiringpo',
        templateUrl: '/static/components/admin/components/dashboard/views/expiring_po_list.html',
        controller: 'dashboardController',
        controllerAs: 'adminDashboardScope',
    })

     .state('listmanagerpo',{
        url: '/listmanagerpo/:obj',
        templateUrl: '/static/components/admin/components/dashboard/views/listmanagerpo.html',
        controller: 'dashboardController',
        controllerAs: 'adminDashboardScope',
    })


    .state('listmanagerexppo',{
        url: '/listmanagerexppo/:obj',
        templateUrl: '/static/components/admin/components/dashboard/views/listmanagerexppo.html',
        controller: 'dashboardController',
        controllerAs: 'adminDashboardScope',
    })


//    show manager resignation start

    .state('listmanagerresignations',{
        url: '/listmanagerresignations/:obj',
        templateUrl: '/static/components/admin/components/dashboard/views/listmanagerresignations.html',
        controller: 'dashboardController',
        controllerAs: 'adminDashboardScope',
    })

// show manager resignation ends


// businessUnitMaster starts
    .state('addbusinessunitmaster',{
        url: '/addbusinessunitmaster',
        templateUrl: '/static/components/admin/components/businessunitmaster/views/addbusinessunitmaster.html',
        controller: 'businessUnitMasterController',
        controllerAs: 'businessUnitMasterScope',

    })

    .state('listbusinessunit',{
        url: '/listbusinessunit',
        templateUrl: '/static/components/admin/components/businessunitmaster/views/listbusinessunitmaster.html',
        controller: 'businessUnitMasterController',
        controllerAs: 'businessUnitMasterScope',
    })

    .state('editbusinessunit',{
        url: '/editbusinessunit/:obj',
        templateUrl: '/static/components/admin/components/businessunitmaster/views/editbusinessunit.html',
        controller: 'businessUnitMasterController',
        controllerAs: 'businessUnitMasterScope',
    })
// businessUnitMaster ends

// Currency Master starts

    .state('addcurrencymaster',{
        url: '/addcurrency',
        templateUrl: '/static/components/admin/components/currencymaster/views/addcurrencymaster.html',
        controller: 'currencyMasterController',
        controllerAs: 'currencyMasterScope',
    })

    .state('listcurrencymaster',{
        url: '/listcurrency',
        templateUrl: '/static/components/admin/components/currencymaster/views/listcurrency.html',
        controller: 'currencyMasterController',
        controllerAs: 'currencyMasterScope',
    })

    .state('updatecurrencymaster',{
        url: '/updatecurrency/:obj',
        templateUrl: '/static/components/admin/components/currencymaster/views/editcurrencymaster.html',
        controller: 'currencyMasterController',
        controllerAs: 'currencyMasterScope',
    })

//Currency Master Ends

// office location starts

    .state('addofficelocation',{
        url: '/addofficelocation',
        templateUrl: '/static/components/admin/components/officelocation/views/addofficelocation.html',
        controller: 'officelocationController',
        controllerAs: 'officelocationScope',
    })

    .state('listofficelocation',{
        url: '/listofficelocation',
        templateUrl: '/static/components/admin/components/officelocation/views/listofficelocation.html',
        controller: 'officelocationController',
        controllerAs: 'officelocationScope',
    })

    .state('editofficelocation',{
        url: '/editofficelocation/:obj',
        templateUrl: '/static/components/admin/components/officelocation/views/editofficelocation.html',
        controller: 'officelocationController',
        controllerAs: 'officelocationScope',
    })

//office location ends

//  designationmaster States starts

    .state('adddesignationmaster',{
        url: '/adddesignationmaster',
        templateUrl: '/static/components/admin/components/designationmaster/views/adddesignationmaster.html',
        controller: 'designationController',
        controllerAs: 'designationScope',
    })

    .state('listdesignation',{
        url:'/listdesignation',
        templateUrl:'/static/components/admin/components/designationmaster/views/listdesignation.html',
        controller: 'designationController',
        controllerAs: 'designationScope',
    })

    .state('editdesignation',{
        url:'/editdesignation/:obj',
        templateUrl:'/static/components/admin/components/designationmaster/views/editdesignation.html',
        controller: 'designationController',
        controllerAs: 'designationScope',
    })
//  designationmaster States end here

//  project type master States starts


    .state('addprojecttypemaster',{
        url: '/addprojecttypemaster',
        templateUrl: '/static/components/admin/components/projecttypemaster/views/addprojecttypemaster.html',
        controller: 'projecttypeController',
        controllerAs: 'projecttypeScope',
    })


    .state('listprojecttypemaster',{
        url: '/listprojecttypemaster',
        templateUrl: '/static/components/admin/components/projecttypemaster/views/listprojecttype.html',
        controller: 'projecttypeController',
        controllerAs: 'projecttypeScope',
    })

    .state('editprojecttype',{
        url:'/editprojecttype/:obj',
        templateUrl:'/static/components/admin/components/projecttypemaster/views/editprojecttype.html',
        controller: 'projecttypeController',
        controllerAs: 'projecttypeScope',
    })

    //  project master States starts

    .state('addprojectmaster',{
        url: '/addprojectmaster',
        templateUrl: '/static/components/admin/components/projectmaster/views/addprojectmaster.html',
        controller: 'projectmasterController',
        controllerAs: 'projectmasterScope',
    })

    .state('listprojectmaster',{
        url: '/listprojectmaster',
        templateUrl: '/static/components/admin/components/projectmaster/views/listprojectmaster.html',
        controller: 'projectmasterController',
        controllerAs: 'projectmasterScope',
    })

    .state('editprojectmaster',{
        url:'/editprojectmaster/:obj',
        templateUrl:'/static/components/admin/components/projectmaster/views/editprojectmaster.html',
        controller: 'projectmasterController',
        controllerAs: 'projectmasterScope',
    })

    .state('changeViewPOstate',{
        url:'/changeviewpostate/:obj',
        templateUrl:'/static/components/admin/components/projectmaster/views/listprojectPurchaseOrder.html',
        controller: 'projectmasterController',
        controllerAs: 'projectmasterScope',
    })

    .state('viewcustomerpostate',{
        url:'/viewcustomerpostate/:obj',
        templateUrl:'/static/components/admin/components/customermaster/views/listcustomerprojectpo.html',
        controller: 'customerMasterController',
        controllerAs: 'customerMasterScope',
    })



//    project assignee

     .state('managerprojectassign',{
        url:'/managerprojectassign',
        templateUrl:'/static/components/admin/components/projectAssign/views/projManagerAssign.html',
        controller: 'projectAssignController',
        controllerAs: 'projectAssignScope',
    })

    .state('viewresource',{
        url:'/viewresource/:obj',
        templateUrl:'/static/components/admin/components/projectAssign/views/viewResource.html',
        controller: 'projectAssignController',
        controllerAs: 'projectAssignScope',
    })

    .state('viewdocuments',{
        url:'/viewdocuments/:obj',
        templateUrl:'/static/components/admin/components/projectAssign/views/viewDocuments.html',
        controller: 'projectAssignController',
        controllerAs: 'projectAssignScope',
    })

     .state('listemployeeassignedtomanager',{
        url: '/listemployeeassignedtomanager/:obj',
        templateUrl: '/static/components/admin/components/projectAssign/views/listemployeeassignedtomanager.html',
        controller: 'projectAssignController',
        controllerAs: 'projectAssignScope',
    })




   //  project document States starts

    .state('addprojectdocument',{
        url: '/addprojectdocument',
        templateUrl: '/static/components/admin/components/projectdocuments/views/addprojectdocument.html',
        controller: 'projectdocumentController',
        controllerAs: 'projectdocumentScope',
    })

    .state('listprojectdocument',{
        url: '/listprojectdocument',
        templateUrl: '/static/components/admin/components/projectdocuments/views/listprojectdocument.html',
        controller: 'projectdocumentController',
        controllerAs: 'projectdocumentScope',
    })

    .state('editprojectdocument',{
        url:'/editprojectdocument/:obj',
        templateUrl: '/static/components/admin/components/projectdocuments/views/editprojectdocument.html',
        controller: 'projectdocumentController',
        controllerAs: 'projectdocumentScope',
    })


//billing states start here
  .state('addbilling',{
        url: '/addbilling',
        templateUrl: '/static/components/admin/components/billing/views/addbilling.html',
        controller: 'billingController',
        controllerAs: 'billingScope',
    })

    .state('listbilling',{
        url: '/listbilling',
        templateUrl: '/static/components/admin/components/billing/views/listbilling.html',
        controller: 'billingController',
        controllerAs: 'billingScope',
    })

// Manager Dashboard
    .state('managerdashboard',{
        url: '/managerdashboard/:obj',
        templateUrl: '/static/components/admin/components/dashboard/views/managerDashboard.html',
        controller: 'dashboardController',
        controllerAs: 'adminDashboardScope',
    })


    .state('viewDocuments',{
        url:'/viewDocuments/:obj',
        templateUrl:'/static/components/admin/components/projectmaster/views/viewDocuments.html',
        controller: 'projectmasterController',
        controllerAs: 'projectmasterScope',
    })

    .state('projectassignmanager',{
        url: '/projectassignmanager/:obj',
        templateUrl: '/static/components/admin/components/projectAssign/views/projectassignmanager.html',
        controller: 'projectAssignController',
        controllerAs: 'projectAssignScope',
    })



   //  customer master States starts

    .state('addcustomermaster',{
        url: '/addcustomermaster',
        templateUrl: '/static/components/admin/components/customermaster/views/addcustomermaster.html',
        controller: 'customerMasterController',
        controllerAs: 'customerMasterScope',
    })

    .state('listcustomermaster',{
        url: '/listcustomermaster',
        templateUrl: '/static/components/admin/components/customermaster/views/listcustomermaster.html',
        controller: 'customerMasterController',
        controllerAs: 'customerMasterScope',
    })

    .state('editcustomermaster',{
        url:'/editcustomermaster/:obj',
        templateUrl: '/static/components/admin/components/customermaster/views/editcustomermaster.html',
        controller: 'customerMasterController',
        controllerAs: 'customerMasterScope',
    })

    .state('stateViewProject',{
        url:'/stateviewproject/:obj',
        templateUrl: '/static/components/admin/components/customermaster/views/customerproject.html',
        controller: 'customerMasterController',
        controllerAs: 'customerMasterScope',
    })

//Purchase order


    .state('addpurchaseorder',{
        url: '/addpurchaseorder',
        templateUrl: '/static/components/admin/components/purchaseOrder/views/addPurchaseOrder.html',
        controller: 'purchaseOrderController',
        controllerAs: 'purchaseOrderScope',
    })

    .state('listpurchaseorder',{
        url: '/listpurchaseorder',
        templateUrl: '/static/components/admin/components/purchaseOrder/views/listPurchaseOrder.html',
        controller: 'purchaseOrderController',
        controllerAs: 'purchaseOrderScope',
    })

    .state('editpurchaseorder',{
        url:'/editpurchaseorder/:obj',
        templateUrl: '/static/components/admin/components/purchaseOrder/views/editPurchaseOrder.html',
        controller: 'purchaseOrderController',
        controllerAs: 'purchaseOrderScope',
    })






}])


.controller('checkSessionController',['$rootScope','$http','$state', function($rootScope,$http,$state){

      var count = 0

      $rootScope.checkSession = function(){

      var success = function(response){
         checkSession = response.data.data
         console.log(response.data)
         $rootScope.userRolesToggle = response.data
         if(response.data.empId){
            if(count==0){
                if(response.data.empRole==3){
                    count=count+1
                    $state.go('editemployee',{obj: response.data.empId})
                }

                else if(response.data.empRole==2){
                    count=count+1
                    $state.go('managerdashboard',{obj: response.data.empId})
                }


            }

         }
         else{
             window.location="/";
         }
         console.log('success')
     }

      var failure = function(response){

            console.log(response)
            console.log('failure')
        }

        $http.get('api/checksession/',{
        }).then(success, failure)


 }


 $rootScope.signOut = function(){

    var success = function(response){
         console.log(response.data)
         window.location="/";
         console.log('success')
     }

      var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        $http.get('api/signout/',{
        }).then(success, failure)

 }

}])


