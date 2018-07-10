angular.module('employeeApp.employeeeducationController',[])

.controller('employeeeducationController',['employeeeducationService','$stateParams','$state','$rootScope', function(employeeeducationService,$stateParams,$state,$rootScope){

    var employeeeducationScope = this;

// Save Function

    employeeeducationScope.saveEmployeeeducation = function(){

       var dateOfComplete = employeeeducationScope.dateOfComplete.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");

        empEducationData={
            'empSchoolUnivName' : employeeeducationScope.employeeschooluniversityname,
//            'empRelation' : employeedependentsScope.relation,
            'empQualiDegrName' : employeeeducationScope.qualificationdegreename,
            'empdateOfComplete' : dateOfComplete,
            'empNotes' : employeeeducationScope.notes,


        }

        console.log(empEducationData)

        var success = function(response){

//            employeeeducationScope.employeeschooluniversityname= ""
//            employeeeducationScope.qualificationdegreename= ""
//            employeeeducationScope.dateOfComplete = ""
//            employeeeducationScope.notes = ""
            employeeeducationScope.successmsg = true
            employeeeducationScope.errormsg = false
            console.log(response)
            console.log('success')

        }

        var failure = function(response){

//            employeeeducationScope.employeedependentsname= ""
//            employeeeducationScope.dob= ""
//            employeeeducationScope.relation = ""
            employeeeducationScope.successmsg = false
            employeeeducationScope.errormsg = true
            console.log(response)
            console.log('Failure')

        }

       employeeeducationService.saveEmployeeeducation(empEducationData, success, failure)

    }

    // Listing Function

    employeeeducationScope.getEmployeeeducationlist = function(){

        $rootScope.checkSession()

         id = $stateParams.obj


        var success = function(response){
            employeeeducationScope.listdata = response.data.data
            console.log(employeeeducationScope.listdata)
            console.log('success')

        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        employeeeducationService.listEmployeeeducation(id,success, failure)
    }



    // Delete Function


    employeeeducationScope.deleteemployeeeducation = function(edu_id, $index){

        if (confirm('Are You Sure?')){

            var rowindex = $index

            var success = function(response){
                console.log(response.data.data)
                console.log('success')

                if(response.data.data.response == "success"){
                    employeeeducationScope.listdata.splice(rowindex,1)
                }
            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            employeeeducationService.deleteemployeeeducation(edu_id, success, failure)

        }

    }

     //    change state with id

    employeeeducationScope.changeState = function(id){
        $state.go('editemployeeducation',{obj: JSON.stringify(id)})
    }

// insert data into fields function

    employeeeducationScope.insertdatarow = function(){

        $rootScope.checkSession()

        id = $stateParams.obj
        var success = function(response){
            console.log('success')
            employeeeducationScope.data = response.data.data
            console.log(employeeeducationScope.data)
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        employeeeducationService.geteditdata(id, success, failure)

    }

    employeeeducationScope.updateemployeeeducation = function(){

      var empDoc=employeeeducationScope.data.empDoc.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");

         eduData={
            'id' : employeeeducationScope.data.edu_id,
            'schUnivName' : employeeeducationScope.data.empSchoolUniv_Name,

            'quaDegname' : employeeeducationScope.data.empQuali_Degr_Name,
            'Doc' :empDoc,
            'Notes' : employeeeducationScope.data.empNotes,
        }
        console.log(eduData)

        var success = function(response){

            employeeeducationScope.successmsg = true
            employeeeducationScope.errormsg = false
            console.log(response)
            console.log('success')

        }

        var failure = function(response){

            employeeeducationScope.successmsg = false
            employeeeducationScope.errormsg = true
            console.log(response)
            console.log('failure')

        }
        employeeeducationService.updateemployeeeducation(eduData, success, failure)

     }

      employeeeducationScope.educationrowdata = [];

     employeeeducationScope.educationrow= function(){

        var dateOfComplete = employeeeducationScope.dateOfComplete.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");

        empEducationData={
            'empSchoolUnivName' : employeeeducationScope.employeeschooluniversityname,
            'empQualiDegrName' : employeeeducationScope.qualificationdegreename,
            'empdateOfComplete' : dateOfComplete,
            'empNotes' : employeeeducationScope.notes,
        }

    employeeeducationScope.educationrowdata.push(empEducationData)

    console.log(employeeeducationScope.educationrowdata)
}


   employeeeducationScope.saveemployeeeducation = function(){

   var data = employeeeducationScope.educationrowdata

   console.log(data )

    var success = function(response){
        console.log(response)
        console.log('success')
        employeeeducationScope.successmsg = true
        employeeeducationScope.errormsg = false
    }

    var failure = function(response){
        console.log(response)
        console.log('failure')
        employeeeducationScope.successmsg = false
        employeeeducationScope.errormsg = true
    }

    employeeeducationService.saveEmpEducation(data,success,failure)

}
    return employeeeducationScope;


}])