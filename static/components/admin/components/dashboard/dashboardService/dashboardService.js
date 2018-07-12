angular.module('adminApp.admindashboardService',[])
.service('adminDashboardService',['$http',function($http){

    adminDashboard = {}

    adminDashboard.fetchDashboardVals = function(success,failure){
        $http.get('api/fetchdashboardvalues/').then(success,failure)
    }

    adminDashboard.managerProjectCount = function(id, success, failure){
        $http.post('api/managerprojectcount/',{
            'id':id,
        }).then(success,failure)
    }

    adminDashboard.getexpiringpolist = function(success, failure){
        $http.get('api/getexpiringpolist/').then(success,failure)
    }

    adminDashboard.getManagerPoData = function(id, success, failure){
         $http.get('api/getmanagerpodata/?id='+id).then(success,failure)
    }

    adminDashboard.getManagerExpPoData = function(id, success, failure){
        $http.get('api/getmanagerexpoodata/?id='+id).then(success,failure)
    }

    adminDashboard.getemployeeresignations = function(id, success, failure){
        $http.get('api/ListEmployeeResignations/?id='+id).then(success,failure)
    }

    adminDashboard.editemployeeresignations = function(id, success, failure){
        $http.get('api/editemployeeresignations/?id='+id).then(success,failure)
    }

    adminDashboard.updateEmployeeResignations = function(empResignData, success, failure){

        $http.post('api/updateemployeeresignation/',{
            'id': empResignData.id,
            'resignReason' : empResignData.reasonOfResign,
            'resignDate' : empResignData.resignDate,
            'managerComment':empResignData.managerComment,
        }).then(success, failure)
    }


    return adminDashboard;

}])