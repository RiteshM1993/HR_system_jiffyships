angular.module('employeeApp.empTypeService',[])
.service('empTypeService',['$http',function($http){

    employeeType = {}

    employeeType.saveEmpType = function(empTypeName, success, failure){

        $http.post('/employee/api/saveemptype/',{
            'emptypename' : empTypeName,
        }).then(success,failure)
    }

    employeeType.listingEmpType = function(success, failure){
        $http.get('/employee/api/listemptype/').then(success,failure)
    }

    employeeType.delEmpType = function(id,success, failure){
        $http.delete('/employee/api/delemptype/?id='+id).then(success,failure)
    }

    employeeType.getdataEmpType = function(id,success, failure){
        $http.get('/employee/api/getemptype/?id='+id).then(success,failure)
    }

    employeeType.updateEmpType = function(id,typeName,success, failure){
        $http.post('/employee/api/updateemptype/',{
            'id' : id,
            'emptypename' : typeName,
        }).then(success,failure)
    }

    return employeeType

}])