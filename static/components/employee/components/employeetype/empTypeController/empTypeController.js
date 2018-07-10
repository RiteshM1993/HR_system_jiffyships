angular.module('employeeApp.empTypeController',[])
.controller('empTypeController',['$state','$stateParams','empTypeService','$rootScope',function($state,$stateParams,empTypeService,$rootScope){

    var empTypeScope = this;

    empTypeScope.saveEmployeeType = function(){

        var empTypeName= empTypeScope.empTypeName

        var success = function(response){
            console.log(response)
            console.log('success')
            empTypeScope.successmsg = true
            empTypeScope.errormsg = false
        }

        var failure = function(response){
            empTypeScope.successmsg = false
            empTypeScope.errormsg = true
            console.log(response)
            console.log('failure')
        }

        empTypeService.saveEmpType(empTypeName, success, failure)
    }
    
    empTypeScope.getEmpType = function(){

        $rootScope.checkSession()

        var success = function(response){
            console.log(response)
            console.log('success')
            empTypeScope.data = response.data.data
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
            
        }

        empTypeService.listingEmpType(success, failure)
    }

    empTypeScope.deleteEmpType = function(id, $index){
        if(confirm('Are you sure?')){

            var success = function(response){
                console.log(response)
                console.log('success')
                empTypeScope.data.splice($index,1)
            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            empTypeService.delEmpType(id,success, failure)

        }
    }

    empTypeScope.changetoeditState = function(id){
        $state.go('editemptype',{
            'obj':id
        })
    }

    empTypeScope.getvalues = function(){

        $rootScope.checkSession()
        var id = $stateParams.obj

        var success = function(response){
            console.log(response)
            console.log('success')
            empTypeScope.data = response.data.data
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        empTypeService.getdataEmpType(id,success, failure)
    }

    empTypeScope.updateEmployeeType = function(){
        var id = empTypeScope.data.id
        var typeName = empTypeScope.data.type_name

        var success = function(response){
            console.log(response)
            console.log('success')
            empTypeScope.successmsg = true
            empTypeScope.errormsg = false
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
            empTypeScope.successmsg = false
            empTypeScope.errormsg = true
        }

        empTypeService.updateEmpType(id,typeName,success, failure)
    }

    return empTypeScope;

}])