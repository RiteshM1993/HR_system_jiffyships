angular.module('adminApp.businessUnitMasterService',[])
.service('businessUnitMasterService',['$http', function($http){

    var businessUnitMaster = {};

    businessUnitMaster.addBusinessUnit = function(data, success, failure){
//    console.log(data.managerId)
        $http.post('api/savebusinessunit/',{
            'businessUnitName' : data.businessUnitName,
            'businessParent' : data.businessParent,
            'status' : data.status,
            'managerId' : data.managerId,
        }).then(success, failure)
    }

    businessUnitMaster.listBusinessUnit = function(success, failure){
        $http.get('api/listbusinessunit/').then(success, failure)
    }

    businessUnitMaster.delBusinessUnit = function(id, success, failure){
        $http.delete('api/delbusinessunit/?id='+id).then(success, failure)
    }

    businessUnitMaster.geteditdata = function(id, success, failure){
        $http.get('api/geteditdata/?id='+id).then(success,failure)
    }

    businessUnitMaster.updateBusinessUnit= function(data, success, failure){
        $http.post('api/updatebusinessunit/',{
            'id' : data.id,
            'businessUnitName' : data.businessUnitName,
            'businessParent' : data.businessParent,
            'status' : data.status,
            'manager_id' : data.managerId,
        }).then(success, failure)
    }

    businessUnitMaster.getMultipleManagerList =function(success, failure){
        $http.get('/employee/api/getempname/').then(success, failure)
    }

    return businessUnitMaster;

}])