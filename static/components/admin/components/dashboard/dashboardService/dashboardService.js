angular.module('adminApp.admindashboardService',[])
.service('adminDashboardService',['$http',function($http){

    adminDashboard = {}

    adminDashboard.fetchDashboardVals = function(success,failure){
        $http.get('api/fetchdashboardvalues/').then(success,failure)
    }


    return adminDashboard;

}])