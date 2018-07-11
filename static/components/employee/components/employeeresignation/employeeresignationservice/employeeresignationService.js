angular.module('employeeApp.employeeresignationService',[])

.service('employeeresignationService',['$http', function($http){

    var employeeresign ={};

    employeeresign.saveEmployeeresign = function(empResignData, success, failure){

        $http.post('/employee/api/saveemployeeresign/',{
            'resignReason' : empResignData.reasonOfResign,
            'resignDate' : empResignData.resignDate,

        }).then(success, failure)
    }

    employeeresign.listEmployeeresignation = function(success, failure){
        $http.get('/employee/api/listEmployeeresignation/').then(success, failure)
    }

    employeeresign.deleteemployeeresignation = function(id, success, failure){
        $http.delete('/employee/api/deleteemployeeproject/?id='+emp_proj_id).then(success, failure)
    }

    employeeresign.geteditdata = function(id, success, failure){
        $http.get('/employee/api/myresignation/?id='+id).then(success, failure)
    }


    employeeresign.updateEmployeeResignation = function(empResignData, success, failure){

        $http.post('/employee/api/updateemployeeresignation/',{
            'id': empProjData.id,
            'reason_Of_Resign' : empResignData.reasonOfResign,
            'resign_Date' : empResignData.resignDate,
        }).then(success, failure)
    }

     return employeeresign;

}])
