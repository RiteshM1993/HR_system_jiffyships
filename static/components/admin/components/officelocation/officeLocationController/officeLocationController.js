angular.module('adminApp.officeLocationController',[])

.controller('officelocationController',['officelocationService','$state','$stateParams','$rootScope', function(officelocationService, $state, $stateParams,$rootScope){

    var officelocationScope = this;


    officelocationScope.addOfficeLocation = function(){

        var officeLocation = officelocationScope.officelocation
        var address = officelocationScope.address

        var success = function(response){
            console.log('success')
            console.log(response)
            officelocationScope.successmsg = true
            officelocationScope.errormsg = false
        }

        var failure = function(response){
            console.log('failure')
            console.log(response)
            officelocationScope.successmsg = false
            officelocationScope.errormsg = true
        }

        officelocationService.saveOfficeLocation(officeLocation, address, success, failure)

    }

    officelocationScope.listOfficeLocation = function(){

        $rootScope.checkSession()

        var success = function(response){
            console.log('success')
            console.log(response)
            officelocationScope.officeLocation = response.data.data
        }

        var failure = function(response){
            console.log('failure')
            console.log(response)
        }

        officelocationService.listingOfficeLocation(success, failure)

    }

    officelocationScope.deleteOfficeLocation = function(locationId, $index){
        if(confirm('Are You Sure?')){

            var success = function(response){
                console.log('success')
                console.log(response)
                if(response.data.data = "success"){
                    officelocationScope.officeLocation.splice($index,1)
                }
            }

            var failure = function(response){
                console.log('failure')
                console.log(response)
            }

            officelocationService.deleteOfficeLocation(locationId,success, failure)

        }
    }

    officelocationScope.changeState = function(locationId){
        $state.go('editofficelocation',{
            'obj' : locationId
        })
    }

    officelocationScope.getFieldsValue = function(){

        $rootScope.checkSession()

        var id = $stateParams.obj
         var success = function(response){
                console.log('success')
                console.log(response)
                officelocationScope.populatedata = response.data.data
            }

            var failure = function(response){
                console.log('failure')
                console.log(response)
            }

            officelocationService.geteditOfficeLocation(id,success, failure)
    }

    officelocationScope.updateOfficeLocation = function(){

        var id = officelocationScope.populatedata.locationId
        var officeLocation = officelocationScope.populatedata.officeLocation
        var address = officelocationScope.populatedata.address

        var success = function(response){
            console.log('success')
            console.log(response)
            officelocationScope.successmsg = true
            officelocationScope.errormsg = false
        }

        var failure = function(response){
            console.log('failure')
            console.log(response)
            officelocationScope.successmsg = false
            officelocationScope.errormsg = true
        }

        officelocationService.updateOfficeLocation(id, officeLocation, address, success, failure)

    }

    return officelocationScope;

}])