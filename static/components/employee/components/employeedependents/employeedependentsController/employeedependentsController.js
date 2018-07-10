angular.module('employeeApp.employeedependentsController',[])

.controller('employeedependentsController',['employeedependentsService','$stateParams','$state','$rootScope', function(employeedependentsService,$stateParams,$state,$rootScope){

    var employeedependentsScope = this;

// Save Function

    employeedependentsScope.saveEmployeedependents = function(){

     var dob = employeedependentsScope.dob.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");


        empDependentsData={
            'empDependentsName' : employeedependentsScope.employeedependentsname,
            'empDob' : dob,
            'empRelation' : employeedependentsScope.relation,

        }

        console.log(empDependentsData)

        var success = function(response){
            employeedependentsScope.successmsg = true
            employeedependentsScope.errormsg = false
            console.log(response)
            console.log('success')

        }

        var failure = function(response){
            employeedependentsScope.successmsg = false
            employeedependentsScope.errormsg = true
            console.log(response)
            console.log('Failure')

        }

       employeedependentsService.saveEmployeedependents(empDependentsData, success, failure)

    }

    // Listing Function

     employeedependentsScope.getEmployeedependentslist = function(){

        $rootScope.checkSession()

        id = $stateParams.obj

        var success = function(response){
            console.log(response)
            employeedependentsScope.listdata = response.data.data

        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        employeedependentsService.listEmployeedependents(id,success, failure)
    }


    // Delete Function


    employeedependentsScope.deleteemployeedependents = function(dep_id, $index){

        if (confirm('Are You Sure?')){

            var rowindex = $index

            var success = function(response){
                console.log(response.data.data)
                console.log('success')

                if(response.data.data.response == "success"){
                    employeedependentsScope.listdata.splice(rowindex,1)
                }
            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            employeedependentsService.deleteEmployeedependents(dep_id, success, failure)

        }

    }


    //    change state with id

    employeedependentsScope.changeState = function(id){
        $state.go('editemployeedependents',{obj: JSON.stringify(id)})
    }
// insert data into fields function

    employeedependentsScope.insertdatarow = function(){

        $rootScope.checkSession()

        id = $stateParams.obj

        listdata = []

        var success = function(response){
            console.log('success')

            listdata.push(response.data.data)

            employeedependentsScope.data = listdata
            console.log(employeedependentsScope.data)
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        employeedependentsService.geteditdata(id, success, failure)

    }

    // save updated data function
    employeedependentsScope.updateemployeedependents = function(){

        var dep_dob = employeedependentsScope.data[0].dep_dob.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");


         depData={
            'id' : employeedependentsScope.data[0].dep_id,
            'depName' : employeedependentsScope.data[0].dep_name,
//            'depdob' : employeedependentsScope.data[0].dep_dob,
            'depRelation' : employeedependentsScope.data[0].dep_Relation,
            'depdob' : dep_dob,
        }

        var success = function(response){

            employeedependentsScope.successmsg = true
            employeedependentsScope.errormsg = false
            console.log(response)
            console.log('success')

        }

        var failure = function(response){

            employeedependentsScope.successmsg = false
            employeedependentsScope.errormsg = true
            console.log(response)
            console.log('failure')

        }
        employeedependentsService.updateemployeedependents(depData, success, failure)

    }




    return employeedependentsScope;


}])