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

    adminDashboardScope.managerProjectCount = function(){
        $rootScope.checkSession()
        var id = $stateParams.obj

        var success = function(response){
            console.log('success')
            console.log(response.data.data)
            adminDashboardScope.data = response.data.data
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        adminDashboardService.managerProjectCount(id, success, failure)
    }

    adminDashboardScope.getexpiringpolist = function(){
        $rootScope.checkSession()

        var success = function(response){
            console.log('success')
            console.log(response.data.data)
            adminDashboardScope.listdata = response.data.data
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        adminDashboardService.getexpiringpolist(success, failure)
    }



    adminDashboardScope.getManagerPoData = function(){
        $rootScope.checkSession()

        var id = $stateParams.obj

        var success = function(response){
            console.log('success')
            console.log(response.data.data)
            adminDashboardScope.listdata = response.data.data
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        adminDashboardService.getManagerPoData(id, success, failure)
    }

    adminDashboardScope.getManagerExpPoData = function(){

        $rootScope.checkSession()

        var id = $stateParams.obj

        var success = function(response){
            console.log('success')
            console.log(response.data.data)
            adminDashboardScope.listdata = response.data.data
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        adminDashboardService.getManagerExpPoData(id, success, failure)
    }



     adminDashboardScope.getemployeeresignations = function(){

        $rootScope.checkSession()

        var id = $stateParams.obj

        var success = function(response){
            console.log('success')
            console.log(response.data.data)
            adminDashboardScope.listdata = response.data.data
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        adminDashboardService.getemployeeresignations(id, success, failure)
    }





    return adminDashboardScope;

}])