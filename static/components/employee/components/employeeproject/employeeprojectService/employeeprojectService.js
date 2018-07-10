angular.module('employeeApp.employeeprojectService',[])

.service('employeeprojectService',['$http', function($http){

    var employeeproject ={};

//     employeeproject.employeeNameValues = function(success, failure){
//            $http.get('/dashboard/api/employeenamevalues/').then(success, failure)
//     }

     employeeproject.projecttypemastervalue = function(success, failure){
        $http.get('/employee/api/projecttypemastervalue/').then(success, failure)
     }

    employeeproject.saveEmployeeProject = function(empProjectData, success, failure){

        $http.post('/employee/api/saveemployeeproject/',{
            'emp_id' : empProjectData.emp_id,
            'project_id' : empProjectData.project_id,
            'startDate' : empProjectData.startDate,
            'endDate' : empProjectData.endDate,
            'empdesc' : empProjectData.empdesc,
//            'empcurr' : empProjectData.empcurr,
//            'empBillRate' : empProjectData.empBillRate,

        }).then(success, failure)
    }


    employeeproject.listEmployeeproject = function(success, failure){
        $http.get('/employee/api/listEmployeeproject/').then(success, failure)
    }

    employeeproject.deleteemployeeproject = function(emp_proj_id, success, failure){
        $http.delete('/employee/api/deleteemployeeproject/?id='+emp_proj_id).then(success, failure)
    }

    employeeproject.geteditdata = function(id, success, failure){
        $http.get('/employee/api/geteditemployeeproject/?id='+id).then(success, failure)
    }



    employeeproject.updateEmployeeProject = function(empProjData, success, failure){

        $http.post('/employee/api/updateemployeeproject/',{
            'id': empProjData.id,
            'emp_id' : empProjData.emp_name,
            'project_id' : empProjData.project_id,
            'start_date' : empProjData.start_date,
            'end_date' : empProjData.end_date,
            'emp_desc' : empProjData.emp_desc,
//            'currencyName' :empProjData.empcurr,
//            "ratePerHour" :empProjData.empBillRate,

        }).then(success, failure)
    }

    employeeproject.getStartEndDate = function(projectId, success, failure){
        $http.get('/employee/api/getstartenddate/?id='+projectId).then(success, failure)
    }

     return employeeproject;

}])