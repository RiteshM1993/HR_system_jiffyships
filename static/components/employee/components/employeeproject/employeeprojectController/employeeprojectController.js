angular.module('employeeApp.employeeprojectController',[])

.controller('employeeprojectController',['employeeprojectService','$stateParams','$state','$http','$rootScope', function(employeeprojectService,$stateParams,$state,$http,$rootScope){

    var employeeprojectScope = this;

    employeeprojectScope.getvalues = function(){

        $rootScope.checkSession()

        getProjecttypemasteridValues = function(){

            var success = function(response){
                employeeprojectScope.projecTypeMasterValue = response.data.data
            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            employeeprojectService.projecttypemastervalue(success, failure)

        }
        getProjecttypemasteridValues()
    }


// Save Function

    employeeprojectScope.saveEmployeeproject = function(){

      var startDate = employeeprojectScope.startDate.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");
      var endDate = employeeprojectScope.endDate.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");

        empProjectData={
            'emp_id' : employeeprojectScope.emp_id,
            'project_id' : employeeprojectScope.project_id,
            'startDate' : startDate,
            'endDate' : endDate,
            'empdesc' : employeeprojectScope.empdesc,
//            'empcurr' : employeeprojectScope.empcurr,
//            'empBillRate' :employeeprojectScope.empBillRate,
        }


        var success = function(response){

            if (response.data.data.data == "employee already assigned to this project"){
                employeeprojectScope.successmsg = false
                employeeprojectScope.errormsg = false
                employeeprojectScope.useralreadyassigned = true
            }
            else{
                employeeprojectScope.successmsg = true
                employeeprojectScope.errormsg = false
                employeeprojectScope.useralreadyassigned = false
            }


            console.log(response.data.data)
            console.log('success')

        }

        var failure = function(response){

            employeeprojectScope.successmsg = false
            employeeprojectScope.errormsg = true
            employeeprojectScope.useralreadyassigned = false
            console.log(response)
            console.log('Failure')

        }

      employeeprojectService.saveEmployeeProject(empProjectData, success, failure)

}
     employeeprojectScope.autoCompleteOptions = {

            minimumChars: 1,
            data: function (searchText) {
            searchName= angular.lowercase(searchText)
                return $http.get('/employee/api/employeenamevalues/?name='+searchName)
                    .then(function (response) {
                        var data = response.data.data
                        console.log(data)
                        dataobj = []
                        for(i = 0; i < data.length; i++){
                        dataobj.push({
                          'empName_email': data[i].emp_name+' ('+data[i].email_id+') '+data[i].emp_id,
                        })
                    }
                        return _.map(dataobj, 'empName_email');
                    });
            },



            itemSelected: function (e) {
                  var extractId = e.item.split(" ")
                  console.log(extractId)
                  console.log(extractId[extractId.length - 1])
                  employeeprojectScope.emp_id = extractId[extractId.length - 1]
            }
        }

        // Listing Function

    employeeprojectScope.getEmployeeProjectlist = function(){

        $rootScope.checkSession()

        var success = function(response){
            employeeprojectScope.listdata = response.data.data
            console.log(employeeprojectScope.listdata)
            console.log('success')

        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        employeeprojectService.listEmployeeproject(success, failure)
    }
     // Delete Function

    employeeprojectScope.deleteemployeeproject = function(emp_proj_id, $index){

        if (confirm('Are You Sure?')){

            var rowindex = $index

            var success = function(response){
                console.log(response.data.data)
                console.log('success')

                if(response.data.data.response == "success"){
                    employeeprojectScope.listdata.splice(rowindex,1)
                }
            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            employeeprojectService.deleteemployeeproject(emp_proj_id, success, failure)

        }

    }

    //    change state with id

    employeeprojectScope.changeState = function(id){
        $state.go('editemployeeproject',{obj: id})
    }


        // insert data into fields function

    employeeprojectScope.insertdatarow = function(){

        $rootScope.checkSession()

        id = $stateParams.obj

        var success = function(response){
            console.log('success')
            employeeprojectScope.getvalues()

            employeeprojectScope.data = response.data.data
            console.log(employeeprojectScope.data)
            employeeprojectScope.employee_id = response.data.data.emp_id
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        employeeprojectService.geteditdata(id, success, failure)

    }



    // save updated data function
    employeeprojectScope.updateEmployeeproject = function(){

       var start_date = employeeprojectScope.data.start_date.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");
       var end_date = employeeprojectScope.data.end_date.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");

        console.log(employeeprojectScope.emp_id)

        if (employeeprojectScope.emp_id == null){
            console.log('blank')
            console.log(employeeprojectScope.employee_id)
        }
        else{
            employeeprojectScope.employee_id= employeeprojectScope.emp_id
        }

        empProjData={
            'id' : employeeprojectScope.data.emp_proj_id,
            'emp_name' : employeeprojectScope.employee_id,
            'project_id' : employeeprojectScope.data.project_id,
            'start_date': start_date,
            'end_date' :end_date,
            'emp_desc' : employeeprojectScope.data.emp_desc,
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

        employeeprojectService.updateEmployeeProject(empProjData, success, failure)
    }

    employeeprojectScope.getStartEndDate = function(projectId){

         var success = function(response){
            employeeprojectScope.startDate = response.data.data[0].startDate
            employeeprojectScope.endDate = response.data.data[0].endDate
            console.log(response)
            console.log('success')

        }

        var failure = function(response){

            console.log(response)
            console.log('failure')

        }

        employeeprojectService.getStartEndDate(projectId, success, failure)

    }


     employeeprojectScope.checkErr = function(startDate,endDate) {
            employeeprojectScope.errMessage = '';
            var curDate = new Date();

            if(new Date(startDate) < new Date(endDate)){

                employeeprojectScope.errMessage = true
                employeeprojectScope.error_msg = false

              return false;
            }

             if(new Date(startDate) > new Date(endDate)){
                  employeeprojectScope.errMessage = false
                  employeeprojectScope.error_msg = true

               return false;

           }

        };


    return employeeprojectScope;


}])