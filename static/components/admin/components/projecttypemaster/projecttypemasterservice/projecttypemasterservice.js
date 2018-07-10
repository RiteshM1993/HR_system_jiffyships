angular.module('adminApp.projecttypeService',[])

.service('projecttypeService',['$http', function($http){

    var project ={};

    project.addProjecttype = function(projecttypename,success, failure){

        $http.post('api/saveprojecttype/',{
            'proj_name' : projecttypename,

        }).then(success, failure)
    }

    project.listProjecttype = function(success, failure){
            $http.get('api/listprojecttype/').then(success, failure)
    }


    project.deleteProjecttype = function(proj_id, success, failure){
         $http.delete('api/deleteprojecttype/?id='+proj_id).then(success, failure)
    }

    project.geteditdata = function(id, success, failure){
        $http.get('api/geteditprojecttypedata/?id='+id).then(success, failure)
    }
    project.updateProjecttype = function(projectData, success, failure){
        $http.post('api/getupdateprojecttype/',{
            'id': projectData.projid,
            'proj_name' : projectData.projName,
        }).then(success, failure)
    }

    return project;
}])

