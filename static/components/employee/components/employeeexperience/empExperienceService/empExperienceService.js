angular.module('employeeApp.empExperienceService',[])

.service('empexperienceService',['$http', function($http){

    var empexperience = {};

    empexperience.saveEmpExperience = function(data,success,failure){
        $http.post('/employee/api/saveEmpExperience/',{
            'data' : data,
        }).then(success,failure)
    }

    empexperience.listEmpExperience = function(id,success,failure){
        $http.get('/employee/api/listempexperience/?id='+id).then(success,failure)
    }

    empexperience.delEmpExperience = function(id,success,failure){
        $http.delete('/employee/api/delempexperience/?id='+id).then(success,failure)
    }

    empexperience.geteditEmpExperiencedata = function(id,success,failure){
        $http.post('/employee/api/geteditEmpExperiencedata/',{
            'id' : id,
        }).then(success,failure)
    }

    empexperience.updatedataEmpExperiencedata = function(data,success,failure){
        $http.post('/employee/api/updateEmpExperiencedata/',{
            'id': data.id,
            'prevCompanyName' : data.prevCompanyName,
            'jobTitle' : data.jobTitle,
            'fromDate' : data.fromDate,
            'toDate' : data.toDate,
            'jobDescription' : data.jobDescription,
        }).then(success,failure)
    }

    return empexperience;

}])