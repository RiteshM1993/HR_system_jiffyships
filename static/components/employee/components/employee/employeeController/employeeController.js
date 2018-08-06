angular.module('employeeApp.employeeController',[])

.controller('employeeController',['employeeService','$stateParams','$state','$http','$rootScope', function(employeeService,$stateParams,$state,$http,$rootScope){

    var employeeScope = this;

//  get save page values

        $rootScope.checkSession()


// Save Function

    employeeScope.saveEmployee = function(){

//        var dob = employeeScope.dob.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");

        var formdata = new FormData();

        formdata.append('file', employeeScope.empImage);
        formdata.append('empFirstName', employeeScope.employeefirstname);
        formdata.append('empMiddleName', employeeScope.employeemiddlename);
        formdata.append('empLastName', employeeScope.employeelastname);
        formdata.append('empEmail', employeeScope.email);
        formdata.append('empMobNum', employeeScope.mobilenum);
        formdata.append('experience', employeeScope.experience);
        formdata.append('empCurrAddr', employeeScope.curraddr);
        formdata.append('empPermaAddr', employeeScope.permaaddr);
        formdata.append('dmEmpID', employeeScope.dmEmployeeId);
        formdata.append('empRole', employeeScope.empRole);



        var success = function(response){
            employeeScope.successmsg = true
            employeeScope.errormsg = false
            console.log(response)
            console.log('success')

        }

        var failure = function(response){
            employeeScope.successmsg = false
            employeeScope.errormsg = true
            console.log(response)
            console.log('failure')

        }

        employeeService.saveEmployee(formdata, success, failure)

    }

// Listing Function

    employeeScope.getEmployeelist = function(){

        $rootScope.checkSession()

        var success = function(response){
            employeeScope.listdata = response.data.data
            console.log(employeeScope.listdata)
            console.log('success')

        }

        var failure = function(response){

            console.log(response)
            console.log('failure')

        }

        employeeService.listEmployee(success, failure)
    }

// Delete function

    employeeScope.deleteEmployee = function (emp_id, $index){
        if (confirm('Are You Sure?')){
            var rowindex = $index

        var success = function(response){

            if(response.data.data.successmsg == "success"){
                employeeScope.listdata.splice(rowindex,1)
            }

            console.log(response.data.data.successmsg)
            console.log('success')

        }

        var failure = function(response){

            console.log(response)
            console.log('failure')

        }

            employeeService.deleteEmployee(emp_id, success, failure)
        }

    }

//    change state with id

    employeeScope.changeState = function(id){
        $state.go('editemployee',{obj: JSON.stringify(id)})
    }
// insert data into fields function

    employeeScope.insertdatarow = function(){

        $rootScope.checkSession()

        id = $stateParams.obj

        var success = function(response){
            employeeScope.data = response.data.data
            console.log(employeeScope.data)

        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }



        employeeService.geteditdata(id, success, failure)

    }

// save updated data function
    employeeScope.updateEmployee = function(){


       var formdata = new FormData();

        formdata.append('file', employeeScope.data.emp_Image);
        formdata.append('empFirstName', employeeScope.data.first_name);
        formdata.append('empMiddleName', employeeScope.data.middle_name);
        formdata.append('empLastName', employeeScope.data.last_name);
        formdata.append('EmpId', employeeScope.data.EmpId);
        formdata.append('empEmail', employeeScope.data.emp_email);
        formdata.append('empMobNum', employeeScope.data.mobile_number);
        formdata.append('experience', employeeScope.data.year_exp);
        formdata.append('empCurrAddr', employeeScope.data.emp_curr_addr);
        formdata.append('empPermaAddr', employeeScope.data.emp_per_addr);
        formdata.append('empRole', employeeScope.data.emp_role);
        formdata.append('id', employeeScope.data.emp_id);


        var success = function(response){
            employeeScope.successmsg = true
            employeeScope.errormsg = false
            console.log(response)
            console.log('success')

        }

        var failure = function(response){
            employeeScope.successmsg = false
            employeeScope.errormsg = true
            console.log(response)
            console.log('failure')

        }

        employeeService.updateEmployee(formdata, success, failure)


    }

//    Advance Search





    employeeScope.clearform = function(){
        employeeScope.data.status_id = ""
        employeeScope.data.jobtitle_id = ""
        employeeScope.data.isactive = ""
        employeeScope.data.businessunit_id = ""
        employeeScope.data.office_locationId = ""
    }



//    employee 360 change state only

    employeeScope.empAllDetailsState = function(emp_id){
         $state.go('empAllDetailsState',{
            'obj':emp_id,
        })
    }



    employeeScope.getEmp360Details = function(){

        $rootScope.checkSession()

        id = $stateParams.obj

        var success = function(response){
            employeeScope.emp360data = response.data.data[0]
            employeeScope.empProjects = response.data.data
            console.log(employeeScope.emp360data)
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        getEmp360IncrementDetails(id)
        getEmp360EducationDetails(id)

        employeeService.getEmp360Details(id, success, failure)
    }


    getEmp360IncrementDetails = function(id){


        var success = function(response){
            employeeScope.emp360Incrementdata = response.data.data

            console.log(employeeScope.emp360Incrementdata)
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        employeeService.getEmp360IncrementDetails(id, success, failure)
    }

    getEmp360EducationDetails = function(id){

        var success = function(response){

            employeeScope.emp360EducationData = response.data.data

            console.log(employeeScope.emp360EducationData)
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        employeeService.getEmp360EducationDetails(id, success, failure)
    }





    return employeeScope;

}])



.directive('fileModel',['$parse', function($parse){
    return{
        restrict: 'A',
        link: function(scope,element,attrs){
              var model=$parse(attrs.fileModel);
              var modelSetter = model.assign;

              element.bind('change', function(){
                scope.$apply(function(){
                modelSetter(scope, element[0].files[0]);
                   });
              });
           }
        };
     }]);

