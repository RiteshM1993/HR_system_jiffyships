angular.module('employeeApp.emp_designationpackagehistoryService',[])
.service('empdesigpackhistoryService',['$http', function($http){
    empdesigpackhistory = {}
//    add emp history get pre filled values starts
    empdesigpackhistory.getEmployeeName = function(success, failure){
        $http.get('/employee/api/getempname/').then(success, failure)
    }

    empdesigpackhistory.getDesignation = function(success, failure){
        $http.get('/employee/api/employeedesignationvalues/').then(success, failure)
    }

    empdesigpackhistory.getCurrency = function(success, failure){
        $http.get('/employee/api/getcurrency/').then(success, failure)
    }
//    add emp history get pre filled values ends

    empdesigpackhistory.saveempdesigpackhistory = function(data, success, failure){
        $http.post('/employee/api/saveemp_desig_pack_history/',{
            'emp_id' : data.emp_id,
            'salary' : data.salary,
            'from_date' : data.from_date,
            'to_date' : data.to_date,
            'active' : data.active,
            'currency_id' : data.currency_id,
            'designation_id' : data.designation_id,
        }).then(success, failure)
    }

    empdesigpackhistory.listempdesigpackhistory = function(id,success, failure){
        $http.get('/employee/api/listempdesigpackhistory/?id='+id).then(success, failure)
    }

    empdesigpackhistory.delEmployeeHistory = function(id,success, failure){
        $http.post('/employee/api/delempdesigpackhistory/?id='+id).then(success, failure)
    }

    empdesigpackhistory.getpopulateEditData = function(id,success, failure){
        $http.get('/employee/api/getempdesigpackhistoryeditdata/?id='+id).then(success, failure)
    }

    empdesigpackhistory.updateempdesigpackhistory = function(data, success, failure){
        $http.post('/employee/api/updateempdesigpackhistory/',{
            'empdesigpack_id': data.empdesigpack_id,
            'emp_id' : data.emp_id,
            'salary' : data.salary,
            'from_date' : data.from_date,
            'to_date' : data.to_date,
            'active' : data.active,
            'currency_id' : data.currency_id,
            'designation_id' : data.designation_id,
        }).then(success, failure)
    }

    return empdesigpackhistory
}])