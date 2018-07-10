angular.module('adminApp.designationService',[])

.service('designationService',['$http', function($http){

    var designation ={};

    designation.addDesignation = function(designationname,success, failure){

        $http.post('api/savedesignation/',{
            'des_name' : designationname,

        }).then(success, failure)
    }

    designation.listDesignation = function(success, failure){
            $http.get('api/listdesignation/').then(success, failure)
    }

    designation.deleteDesignation = function(des_id, success, failure){
         $http.delete('api/deletedesignation/?id='+des_id).then(success, failure)
    }

    designation.geteditdata = function(id, success, failure){
        $http.get('api/geteditdesignationdata/?id='+id).then(success, failure)
    }

    designation.updateDesignation = function(desData, success, failure){
        $http.post('api/updatedesignation/',{
            'id': desData.desid,
            'des_name' : desData.desName,
        }).then(success, failure)
    }

    return designation;

}])

