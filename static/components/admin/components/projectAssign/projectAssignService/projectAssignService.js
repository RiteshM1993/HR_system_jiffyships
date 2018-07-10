angular.module('adminApp.projectAssignService',[])
.service('projectAssignService',['$http', function($http){
    var projectAssign = {};

    projectAssign.listingProjectManager = function(success, failure){
        $http.get('api/listprojectmaster/').then(success, failure)
    }

    projectAssign.getResource = function(id, success, failure){
        $http.get('api/getresources/?id='+id).then(success, failure)
    }

    projectAssign.getDocuments = function(id, success, failure){
        $http.get('api/getdocuments/?id='+id).then(success, failure)
    }
    projectAssign.listProjectManagerEmpAssigned = function(id, success, failure){
        $http.post('api/listprojectmanagerempassigned/',{
            'id':id,
        }).then(success,failure)
    }

    return projectAssign;

}])