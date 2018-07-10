angular.module('employeeApp.employeeService',[])

.service('employeeService',['$http', function($http){

    var employee ={};

    //    get add employee page data api's

     employee.employeeDesignation = function(success, failure){
            $http.get('/employee/api/employeedesignationvalues/').then(success, failure)
     }

     employee.employeeBusinessUnitValues = function(success, failure){
        $http.get('/employee/api/employeebusinessunitvalues/').then(success, failure)
     }

     employee.employeeOfficeLocationValue = function(success, failure){
        $http.get('/employee/api/employeeofficelocationvalue/').then(success, failure)
     }

     employee.employeeType = function(success, failure){
        $http.get('/employee/api/listemptype/').then(success, failure)
     }

    employee.saveEmployee = function(formdata, success, failure){
        $http({
            method:'POST',
            url:'/employee/api/saveemployee/',
            data:formdata,
                transformRequest: angular.identity,
                headers: {'Content-Type': undefined}
        }).then(success, failure)
    }

    employee.listEmployee = function(success, failure){
        $http.get('/employee/api/listemployee/').then(success, failure)
    }

    employee.deleteEmployee = function(emp_id, success, failure){
         $http.delete('/employee/api/delemployee/?id='+emp_id).then(success, failure)
    }

    employee.geteditdata = function(id, success, failure){
        $http.get('/employee/api/geteditemployeedata/?id='+id).then(success, failure)
    }

    employee.updateEmployee = function(formdata, success, failure){

         $http({
            method:'POST',
            url:'/employee/api/updateemployee/',
            data:formdata,
                transformRequest: angular.identity,
                headers: {'Content-Type': undefined}
        }).then(success, failure)

    }


//    timeline employee

    employee.getEmp360Details = function(id, success, failure){
        $http.get('/employee/api/getEmp360Details/?id='+id).then(success, failure)
    }

    employee.getEmp360IncrementDetails = function(id, success, failure){
        $http.get('/employee/api/getEmp360IncrementDetails/?id='+id).then(success, failure)
    }

    employee.getEmp360EducationDetails  =function(id, success, failure){
        $http.get('/employee/api/getEmp360EducationDetails/?id='+id).then(success, failure)
    }

    employee.advanceSearch = function(columnName, searchText, dbCondition, success, failure){
        $http.post('/employee/api/advancesearch/',{
            'column_name': columnName,
            'search_text': searchText,
            'db_condition': dbCondition,
        }).then(success, failure)
    }

    return employee;

}])