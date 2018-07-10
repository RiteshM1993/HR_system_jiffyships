angular.module('employeeApp.employeedependentsService',[])

.service('employeedependentsService',['$http', function($http){

    var employeedependents ={};

    employeedependents.saveEmployeedependents = function(empDependentsData, success, failure){

        $http.post('/employee/api/saveemployeedependents/',{
            'emp_DependentsName' : empDependentsData.empDependentsName,
            'emp_Relation' : empDependentsData.empRelation,
            'emp_Dob' : empDependentsData.empDob,
        }).then(success, failure)
    }

    employeedependents.listEmployeedependents = function(id,success, failure){
        $http.get('/employee/api/listemployeedependents/?id='+id).then(success, failure)
    }

    employeedependents.deleteEmployeedependents = function(dep_id, success, failure){
        $http.delete('/employee/api/deleteemployeedependents/?id='+dep_id).then(success, failure)
    }
    employeedependents.geteditdata = function(id, success, failure){
        $http.get('/employee/api/geteditemployeedependentsdata/?id='+id).then(success, failure)
    }

    employeedependents.updateemployeedependents= function(depData,success, failure){
        $http.post('/employee/api/updateemployeedependents/',{
            'id' : depData.id,
            'depName' : depData.depName,
            'depRelation' : depData.depRelation,
            'depdob' : depData.depdob,

        }).then(success, failure)
    }


    return employeedependents;

}])