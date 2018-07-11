angular.module('employeeApp',[
    'ui.router',
    'smart-table',
    'autoCompleteModule',
    'employeeApp.employee',
    'employeeApp.emp_designationpackagehistory',
    'employeeApp.empExperience',
    'employeeApp.emptype',
    'employeeApp.employeedependents',
    'employeeApp.employeeEducation',
    'employeeApp.employeeproject',
    'employeeApp.empDoc',
    'employeeApp.employeeresignation',

])

.config(['$stateProvider','$urlRouterProvider', function($stateProvider, $urlRouterProvider){


    $urlRouterProvider.otherwise('/employeedashboard');

    $stateProvider
    .state('employeedashboard',{
        url: '/employeedashboard',
        templateUrl: '/static/components/employee/components/dashboard/views/employeedashboard.html',
    })

//   Employee module starts here

    .state('addemployee',{
        url: '/addemployee',
        templateUrl: '/static/components/employee/components/employee/views/addEmployee.html',
        controller: 'employeeController',
        controllerAs: 'employeeScope',
    })

    .state('listemployee',{
        url:'/listemployee',
        templateUrl:'/static/components/employee/components/employee/views/listEmployee.html',
        controller: 'employeeController',
        controllerAs: 'employeeScope',
    })

    .state('editemployee',{
        url:'/editemployee/:obj',
        templateUrl:'/static/components/employee/components/employee/views/editEmployee.html',
        controller: 'employeeController',
        controllerAs: 'employeeScope',
    })


    // empTimeLine

    .state('empAllDetailsState',{
        url: '/emp360details/:obj',
        templateUrl: '/static/components/employee/components/employee/views/empTimeline.html',
        controller: 'employeeController',
        controllerAs: 'employeeScope',
    })

//    Employee module ends here


// emp_designation package history starts
    .state('addempdesig_pack_history',{
        url: '/addempdesig_pack_history',
        templateUrl: '/static/components/employee/components/emp_designationpackagehistory/views/addemp_designationpackagehistory.html',
        controller: 'empdesigpackhistoryController',
        controllerAs: 'empdesigpackhistoryScope',
    })

    .state('listempdesig_pack_history',{
        url: '/listempdesig_pack_history',
        templateUrl: '/static/components/employee/components/emp_designationpackagehistory/views/listempdesigpackhistory.html',
        controller: 'empdesigpackhistoryController',
        controllerAs: 'empdesigpackhistoryScope',
    })

    .state('editempdesig_pack_history',{
        url: '/editempdesig_pack_history/:obj',
        templateUrl: '/static/components/employee/components/emp_designationpackagehistory/views/editempdesigpackhistory.html',
        controller: 'empdesigpackhistoryController',
        controllerAs: 'empdesigpackhistoryScope',
    })

    .state('empdesig_pack_history',{
        url: '/empdesig_pack_history/:obj',
        templateUrl: '/static/components/employee/components/emp_designationpackagehistory/views/listempdesigpackhistory.html',
        controller: 'empdesigpackhistoryController',
        controllerAs: 'empdesigpackhistoryScope',
    })
// emp_designation package history ends


//emp experience starts

    .state('addempexperience',{
        url: '/addempexperience',
        templateUrl: '/static/components/employee/components/employeeexperience/views/addempexperience.html',
        controller: 'empexperienceController',
        controllerAs: 'empExperienceScope',
    })

    .state('listempexperience',{
        url: '/listempexperience',
        templateUrl: '/static/components/employee/components/employeeexperience/views/listempexperience.html',
        controller: 'empexperienceController',
        controllerAs: 'empExperienceScope',
    })

    .state('editempexperience',{
        url: '/editempexperience/:obj',
        templateUrl: '/static/components/employee/components/employeeexperience/views/editempexperience.html',
        controller: 'empexperienceController',
        controllerAs: 'empExperienceScope',
    })

    .state('empexperience',{
        url: '/empexperience/:obj',
        templateUrl: '/static/components/employee/components/employeeexperience/views/listempexperience.html',
        controller: 'empexperienceController',
        controllerAs: 'empExperienceScope',
    })


//emp experience ends

//emp type starts
    .state('addemptype',{
        url: '/addemptype',
        templateUrl: '/static/components/employee/components/employeetype/views/addemptype.html',
        controller: 'empTypeController',
        controllerAs: 'empTypeScope',
    })

    .state('listemptype',{
        url: '/listemptype',
        templateUrl: '/static/components/employee/components/employeetype/views/listemptype.html',
        controller: 'empTypeController',
        controllerAs: 'empTypeScope',
    })

    .state('editemptype',{
        url: '/editemptype/:obj',
        templateUrl: '/static/components/employee/components/employeetype/views/editemptype.html',
        controller: 'empTypeController',
        controllerAs: 'empTypeScope',
    })


//emp type ends

//ritesh

//    addemployeedependents States start here

    .state('addemployeedependents',{
        url: '/addemployeedependents',
        templateUrl: '/static/components/employee/components/employeedependents/views/addemployeedependents.html',
        controller: 'employeedependentsController',
        controllerAs: 'employeedependentsScope',
    })


    .state('listemployeedependents',{
        url: '/listemployeedependents',
        templateUrl: '/static/components/employee/components/employeedependents/views/listemployeedependents.html',
        controller: 'employeedependentsController',
        controllerAs: 'employeedependentsScope',
    })

    .state('editemployeedependents',{
        url: '/editemployeedependents/:obj',
        templateUrl: '/static/components/employee/components/employeedependents/views/editemployeedependents.html',
        controller: 'employeedependentsController',
        controllerAs: 'employeedependentsScope',
    })

    .state('employeedependents',{
        url: '/employeedependents/:obj',
        templateUrl: '/static/components/employee/components/employeedependents/views/listemployeedependents.html',
        controller: 'employeedependentsController',
        controllerAs: 'employeedependentsScope',
    })


    //    addemployeedependents  ends here

// employee education starts

    .state('addemployeeeducation',{
        url: '/addemployeeeducation',
        templateUrl: '/static/components/employee/components/employeeeducation/views/addemployeeeducation.html',
        controller: 'employeeeducationController',
        controllerAs: 'employeeeducationScope',
    })

    .state('listemployeeeducation',{
        url: '/listemployeeeducation',
        templateUrl: '/static/components/employee/components/employeeeducation/views/listemployeeeducation.html',
        controller: 'employeeeducationController',
        controllerAs: 'employeeeducationScope',
    })

    .state('editemployeeducation',{
        url: '/editemployeeducation/:obj',
        templateUrl: '/static/components/employee/components/employeeeducation/views/editemployeeeducation.html',
        controller: 'employeeeducationController',
        controllerAs: 'employeeeducationScope',
    })

    .state('employeeducation',{
        url: '/employeeducation/:obj',
        templateUrl: '/static/components/employee/components/employeeeducation/views/listemployeeeducation.html',
        controller: 'employeeeducationController',
        controllerAs: 'employeeeducationScope',
    })

// employee education ends


//add employeeproject start here

    .state('addemployeeproject',{
        url:  '/addemployeeproject',
        templateUrl: '/static/components/employee/components/employeeproject/views/addemployeeproject.html',
        controller: 'employeeprojectController',
        controllerAs: 'employeeprojectScope',
    })


    .state('listemployeeproject',{
        url: '/listemployeeproject',
        templateUrl: '/static/components/employee/components/employeeproject/views/listemployeeproject.html',
        controller: 'employeeprojectController',
        controllerAs: 'employeeprojectScope',
    })

  .state('editemployeeproject',{
        url: '/editemployeeproject/:obj',
        templateUrl: '/static/components/employee/components/employeeproject/views/editemployeeproject.html',
        controller: 'employeeprojectController',
        controllerAs: 'employeeprojectScope',
    })

// Emp Doc
.state('addemployeedoc',{
        url:  '/addemployeedoc',
        templateUrl: '/static/components/employee/components/emp_doc/views/addempdoc.html',
        controller: 'empDocController',
        controllerAs: 'empDocScope',
    })
.state('listdoc',{
        url:  '/listdoc',
        templateUrl: '/static/components/employee/components/emp_doc/views/listdoc.html',
        controller: 'empDocController',
        controllerAs: 'empDocScope',
    })

.state('editempdoc',{
    url: '/editempdoc/:obj',
    templateUrl: '/static/components/employee/components/emp_doc/views/editempdoc.html',
    controller: 'empDocController',
    controllerAs: 'empDocScope',
})

//Resignations states starts here

.state('addemployeeresignation',{
      url:  '/addemployeeresignation',
      templateUrl: '/static/components/employee/components/employeeresignation/views/addemployeeresignation.html',
      controller: 'employeeresignationController',
      controllerAs: 'employeeresignationScope',

  })

  .state('listemployeeresignation',{
      url: '/listemployeeresignation',
      templateUrl: '/static/components/employee/components/employeeresignation/views/listemployeeresignation.html',
      controller: 'employeeresignationController',
      controllerAs: 'employeeresignationScope',
  })

//  .state('editemployeeresignation',{
//      url: '/editemployeeresignation/:obj',
//      templateUrl: '/static/components/employee/components/employeeresignation/views/editemployeeresignation.html',
//      controller: 'employeeprojectController',
//      controllerAs: 'employeeprojectScope',
//  })

  .state('myresignation',{
      url: '/myresignation/:obj',
      templateUrl: '/static/components/employee/components/employeeresignation/views/myresignation.html',
      controller: 'employeeresignationController',
      controllerAs: 'employeeresignationScope',
  })






}])

.controller('checkSessionController',['$rootScope','$http','$state', function($rootScope,$http,$state){


      $rootScope.checkSession = function(){
      var success = function(response){
         checkSession = response.data.data
         console.log(response.data)
         $rootScope.userRolesToggle = response.data
         if(response.data.mes=="session created"){
            console.log('inside')
             if(response.data.empRole==3){
                $state.go('editemployee',{obj: response.data.empId})
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
 }])