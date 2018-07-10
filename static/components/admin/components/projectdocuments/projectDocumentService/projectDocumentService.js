angular.module('adminApp.projectdocumentService',[])

.service('projectdocumentService',['$http', function($http){


 var projDoc = {};

    projDoc.saveProjectDoc = function(formdata, success, failure){
        $http({
            method:'POST',
            url:'/dashboard/api/saveprodoc/',
            data:formdata,
                transformRequest: angular.identity,
                headers: {'Content-Type': undefined}
        }).then(success, failure)
    }

   projDoc.listProjectDocument = function(success, failure){
        $http.get('/dashboard/api/listprojectdocument/').then(success, failure)
    }


     projDoc.delProjDoc = function(proj_doc_id, success, failure){
        $http.delete('/dashboard/api/delProjDoc/?id='+proj_doc_id).then(success, failure)
    }

    projDoc.insertdatarow = function(id, success, failure){
        $http.get('/dashboard/api/getEditProjdoc/?id='+id).then(success,failure)
    }

    projDoc.updateProjDoc = function(formdata, success, failure){
        $http({
            method:'POST',
            url:'/dashboard/api/updateProjDoc/',
            data:formdata,
                transformRequest: angular.identity,
                headers: {'Content-Type': undefined}
        }).then(success, failure)
    }




        return projDoc;

}])