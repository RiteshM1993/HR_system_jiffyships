angular.module('adminApp',[
    'ui.router',
    'smart-table',
    'autoCompleteModule',
    'multipleSelect',
    'ngMaterial',
    'employeeApp',
    'adminApp.admindashboard',
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



// Manager Dashboard
    .state('managerdashboard',{
        url: '/managerdashboard/:obj',
        templateUrl: '/static/components/admin/components/dashboard/views/managerDashboard.html',
        controller: 'dashboardController',
        controllerAs: 'adminDashboardScope',
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


