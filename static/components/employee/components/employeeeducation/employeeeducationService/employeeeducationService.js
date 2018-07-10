angular.module('employeeApp.employeeeducationService',[])

.service('employeeeducationService',['$http', function($http){

    var employeeeducation ={};

    employeeeducation.saveEmpEducation = function(data,success,failure){
        $http.post('/employee/api/saveEmpEducation/',{
            'data' : data,
        }).then(success,failure)
    }

     employeeeducation.listEmployeeeducation = function(id,success, failure){
        $http.get('/employee/api/listemployeeeducation/?id='+id).then(success, failure)
    }

     employeeeducation.deleteemployeeeducation = function(edu_id, success, failure){
        $http.delete('/employee/api/deleteemployeeducation/?id='+edu_id).then(success, failure)
    }

    employeeeducation.geteditdata = function(id, success, failure){
        $http.get('/employee/api/geteditemployeeeducationdata/?id='+id).then(success, failure)
    }

    employeeeducation.updateemployeeeducation= function(eduData,success, failure){
        $http.post('/employee/api/updateemployeeeducation/',{
            'id' : eduData.id,
            'schUnivName' : eduData.schUnivName,
            'quaDegname' : eduData.quaDegname,
            'Doc' : eduData.Doc,
            'Notes' : eduData.Notes,

        }).then(success, failure)
    }




    return employeeeducation;

}])