angular.module('adminApp.admindashboardController',[])

.controller('dashboardController',['$state','$stateParams','adminDashboardService','$rootScope',function($state,$stateParams,adminDashboardService,$rootScope){

    var adminDashboardScope = this;

    adminDashboardScope.fetchDashboardVals = function(){

        $rootScope.checkSession()

        var success = function(response){
            adminDashboardScope.data = response.data.data
            console.log(adminDashboardScope.data)
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        adminDashboardService.fetchDashboardVals(success, failure)

    }


    return adminDashboardScope;

}])