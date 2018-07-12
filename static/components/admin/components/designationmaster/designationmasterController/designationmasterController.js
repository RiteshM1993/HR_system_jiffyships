angular.module('adminApp.designationController',[])

.controller('designationController',['designationService','$state','$stateParams','$rootScope', function(designationService,$state,$stateParams,$rootScope){

    var designationScope = this;

    designationScope.saveDesignation = function(){

       var designationname =  designationScope.designationname
        var success = function(response){

            designationScope.successmsg = true
            designationScope.errormsg = false
            console.log(response)
            console.log('success')
        }

        var failure = function(response){

            designationScope.successmsg = false
            designationScope.errormsg = true
            console.log(response)
            console.log('failure')
        }

         designationService.addDesignation(designationname, success, failure)
    }


    // Listing Function

    designationScope.getDesignationlist = function(){

        $rootScope.checkSession()

        var success = function(response){
            designationScope.listdata = response.data.data
            console.log(designationScope.listdata)
            console.log('success')

        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        designationService.listDesignation(success, failure)
    }

    // Delete Function


    designationScope.deleteEmployee = function (des_id, $index){

        if(confirm('Are you sure?')){

            var rowindex = $index

            var success = function(response){

                if(response.data.data.successmsg == "success"){
                    designationScope.listdata.splice(rowindex,1)
                }
                console.log(response.data.data.successmsg)
                console.log('success')

            }
            var failure = function(response){

                console.log(response)
                console.log('failure')

            }

            designationService.deleteDesignation(des_id, success, failure)
        }

    }


    //    change state with id

    designationScope.changeState = function(id){
        $state.go('editemployeeresignation',{obj: JSON.stringify(id)})
    }
// insert data into fields function

    designationScope.insertdatarow = function(){

        $rootScope.checkSession()

        id = $stateParams.obj

        listdata = []

        var success = function(response){
            console.log('success')

            listdata.push(response.data.data)

            designationScope.data = listdata
            console.log(designationScope.data)
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        designationService.geteditdata(id, success, failure)

    }

    // save updated data function
    designationScope.updateDesignation = function(){

         desData={
            'desid' : designationScope.data[0].des_id,
            'desName' : designationScope.data[0].des_name,
        }

        var success = function(response){

            designationScope.successmsg = true
            designationScope.errormsg = false
            console.log(response)
            console.log('success')

        }

        var failure = function(response){

            designationScope.successmsg = false
            designationScope.errormsg = true
            console.log(response)
            console.log('failure')

        }


        designationService.updateDesignation(desData, success, failure)

    }




    return designationScope;


}])