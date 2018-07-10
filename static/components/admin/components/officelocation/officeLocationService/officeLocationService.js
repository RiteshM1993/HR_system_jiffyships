angular.module('adminApp.officeLocationService',[])

.service('officelocationService',['$http', function($http){

    var officelocation = {};

    officelocation.saveOfficeLocation = function(officeLocation, address, success, failure){

        $http.post('api/saveofficelocation/',{
            'officeLocation' : officeLocation,
            'address' : address,
        }).then(success, failure)

    }

    officelocation.listingOfficeLocation = function(success, failure){
        $http.get('api/listofficelocations/').then(success, failure)
    }

    officelocation.deleteOfficeLocation = function(locationId,success, failure){
        $http.get('api/delofficelocations/?id='+locationId).then(success, failure)
    }

    officelocation.geteditOfficeLocation = function(id,success, failure){
        $http.get('api/geteditofficelocations/?id='+id).then(success, failure)
    }

    officelocation.updateOfficeLocation = function(id, officeLocation, address, success, failure){
         $http.post('api/updateofficelocation/',{
            'id' : id,
            'officeLocation' : officeLocation,
            'address' : address,
        }).then(success, failure)

    }

    return officelocation;
}])