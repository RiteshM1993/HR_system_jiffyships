angular.module('employeeApp.empDocService',[])

.service('empDocService',['$http', function($http){

    var empDoc = {};

    empDoc.saveEmpDoc = function(formdata, success, failure){
        $http({
            method:'POST',
            url:'/employee/api/saveempdoc/',
            data:formdata,
                transformRequest: angular.identity,
                headers: {'Content-Type': undefined}
        }).then(success, failure)
    }

    empDoc.listEmpDoc = function(success, failure){
        $http.get('/employee/api/listempdoc/').then(success,failure)
    }

    empDoc.delEmpDoc = function(docId,success, failure){
        $http.delete('/employee/api/delempdoc/?id='+docId).then(success,failure)
    }

    empDoc.geteditEmpDoc = function(id, success, failure){
        $http.get('/employee/api/geteditempdoc/?id='+id).then(success,failure)
    }

    empDoc.updateEmpDoc = function(formdata, success, failure){
        $http({
            method:'POST',
            url:'/employee/api/updateempdoc/',
            data:formdata,
                transformRequest: angular.identity,
                headers: {'Content-Type': undefined}
        }).then(success, failure)
    }


    return empDoc;


}])