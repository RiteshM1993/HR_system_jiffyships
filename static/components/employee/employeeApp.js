angular.module('employeeApp',[
    'ui.router',
    'smart-table',
    'autoCompleteModule',
    'employeeApp.employee',

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




//    Employee module ends here



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