angular.module('employeeApp.employeeresignationController',[])


.controller('employeeresignationController',['employeeresignationService','$stateParams','$state','$rootScope', function(employeeresignationService,$stateParams,$state,$rootScope){

     var employeeresignationScope = this;

     // Save Function

    employeeresignationScope.saveEmployeeresign = function(){

      var resignDate = employeeresignationScope.resignDate.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3/$1/$2");

        empResignData={
            'reasonOfResign' : employeeresignationScope.reasonOfResign,
            'resignDate' : resignDate,
        }

        console.log(empResignData)

        var success = function(response){

            employeeresignationScope.successmsg = true
            employeeresignationScope.errormsg = false
            console.log(response)
            console.log('success')

        }

        var failure = function(response){

            employeeresignationScope.successmsg = false
            employeeresignationScope.errormsg = true
            console.log(response)
            console.log('Failure')

        }

      employeeresignationService.saveEmployeeresign(empResignData, success, failure)

    }

      // Listing Function

    employeeresignationScope.getEmployeeResignationlist = function(){

        console.log('hello ')

        $rootScope.checkSession()

        var success = function(response){
            employeeresignationScope.listdata = response.data.data
            console.log(employeeresignationScope.listdata)
            console.log('success')

        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        employeeresignationService.listEmployeeresignation(success, failure)
    }

    //    change state with id

    employeeresignationScope.changeState = function(id){
        $state.go('myresignation',{obj: id})
    }


        // insert data into fields function

    employeeresignationScope.insertdatarow = function(){

        $rootScope.checkSession()

        id = $stateParams.obj
        listdata = []

        var success = function(response){
            console.log('success')
            //employeeresignationScope.getvalues()
            listdata.push(response.data.data)

            employeeresignationScope.data = listdata
            console.log(employeeprojectScope.data)
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        employeeresignationService.geteditdata(id, success, failure)

    }


    // save updated data function
    employeeresignationScope.updateEmployeeResignation = function(){

       var resignDate = employeeresignationScope.data[0].resignDate.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");

        empResignData={
//            'id' : employeeprojectScope.data[0].emp_proj_id,
            'reasonOfResign' : employeeprojectScope.data[0].emp_id,
            'resignDate': resignDate,
        }

        console.log(empProjData)

        var success = function(response){
            employeeprojectScope.successmsg = true
            employeeprojectScope.errormsg = false
            console.log(response)
            console.log('success')

        }

        var failure = function(response){
            employeeprojectScope.successmsg = false
            employeeprojectScope.errormsg = true
            console.log(response)
            console.log('failure')

        }

        employeeresignationService.updateEmployeeResignation(empResignData, success, failure)
    }


        return employeeresignationScope;



}])
