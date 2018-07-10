angular.module('employeeApp.employeeController',[])

.controller('employeeController',['employeeService','$stateParams','$state','$http','$rootScope', function(employeeService,$stateParams,$state,$http,$rootScope){

    var employeeScope = this;

//  get save page values

    employeeScope.getvalues = function(){

        $rootScope.checkSession()

        getEmployeeType = function(){
            var success = function(response){
                employeeScope.emptypeid = response.data.data

            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            employeeService.employeeType(success, failure)
        }

        getEmployeeType()

        getDesignationValues = function(){

            var success = function(response){
                employeeScope.designationValue = response.data.data

            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            employeeService.employeeDesignation(success, failure)
        }

        getDesignationValues()

        getBusinessUnitValues = function(){

            var success = function(response){
                employeeScope.businessUnitValue= response.data.data

            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            employeeService.employeeBusinessUnitValues(success, failure)
        }

        getBusinessUnitValues()

        getOfficeLocationValue = function(){

            var success = function(response){
                employeeScope.officeLocationValue = response.data.data
            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            employeeService.employeeOfficeLocationValue(success, failure)

        }
        getOfficeLocationValue()
    }


// Save Function

    employeeScope.saveEmployee = function(){

        var dob = employeeScope.dob.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");
        var doj = employeeScope.doj.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");

        if (employeeScope.dol != null){
            var dol = employeeScope.dol.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");
        }

        var formdata = new FormData();

        formdata.append('file', employeeScope.empImage);
        formdata.append('empFirstName', employeeScope.employeefirstname);
        formdata.append('empMiddleName', employeeScope.employeemiddlename);
        formdata.append('empLastName', employeeScope.employeelastname);
        formdata.append('empEmail', employeeScope.email);
        formdata.append('empPersonalEmail', employeeScope.personalemail);
        formdata.append('empMobNum', employeeScope.mobilenum);
        formdata.append('empDob', dob);
        formdata.append('status', employeeScope.emptype);
        formdata.append('jobTitle', employeeScope.jobtitle);
        formdata.append('doj', doj);
        formdata.append('dol', dol);
        formdata.append('officeNumber', employeeScope.officenumber);
        formdata.append('experience', employeeScope.experience);
        formdata.append('businessUnit', employeeScope.businessunit);
        formdata.append('manager', employeeScope.managerEmpId);
        formdata.append('officeLocation', employeeScope.officelocation);
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
            employeeScope.getvalues()

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

       var empId =  employeeScope.data.manager_id
       if(employeeScope.managerEmpId){
          empId =  employeeScope.managerEmpId
       }
       var dob = employeeScope.data.emp_dob.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");
       var doj = employeeScope.data.date_of_joining.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");
        console.log(employeeScope.data.date_of_leaving )
       if (employeeScope.data.date_of_leaving != null){
          var dol = employeeScope.data.date_of_leaving.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");
       }

       else{
            var dol = ""
       }

       var formdata = new FormData();

        formdata.append('file', employeeScope.data.emp_Image);
        formdata.append('empFirstName', employeeScope.data.first_name);
        formdata.append('empMiddleName', employeeScope.data.middle_name);
        formdata.append('empLastName', employeeScope.data.last_name);
        formdata.append('empEmail', employeeScope.data.emp_email);
        formdata.append('empPersonalEmail', employeeScope.data.personal_email);
        formdata.append('empMobNum', employeeScope.data.mobile_number);
        formdata.append('empDob', dob);
        formdata.append('status', employeeScope.data.status_id);
        formdata.append('jobTitle', employeeScope.data.jobtitle_id);
        formdata.append('doj', doj);
        formdata.append('dol', dol);
        formdata.append('officeNumber', employeeScope.data.office_number);
        formdata.append('experience', employeeScope.data.year_exp);
        formdata.append('businessUnit', employeeScope.data.businessunit_id);
        formdata.append('manager', empId);
        formdata.append('officeLocation', employeeScope.data.office_location_id);
        formdata.append('empCurrAddr', employeeScope.data.emp_curr_addr);
        formdata.append('empPermaAddr', employeeScope.data.emp_per_addr);
        formdata.append('id', employeeScope.data.emp_id);
        formdata.append('isActive', employeeScope.data.isactive);
        formdata.append('empRole', employeeScope.data.emp_role);


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

    employeeScope.bindquery = function(){
        employeeScope.dbQuery  = "You are searching for " + "'"+employeeScope.searchText+"' in "+ employeeScope.columnName
    }

    employeeScope.advanceSearch = function(){
        var columnName = employeeScope.columnName
        var searchText = employeeScope.searchText
        var dbCondition = employeeScope.dbCondition

        var success = function(response){

            console.log(response)
            console.log('success')

        }

        var failure = function(response){

            console.log(response)
            console.log('failure')

        }

        employeeService.advanceSearch(columnName, searchText, dbCondition, success, failure)

    }



//    auto complete manager
        employeeScope.autoCompleteOptions = {
            minimumChars: 1,
            data: function (searchText) {
                searchName =angular.lowercase(searchText)
                return $http.get('/employee/api/listmanagerename/?name='+searchName)
                    .then(function (response) {
                        var data = response.data.data
                        dataobj = []
                        for (i = 0; i < data.length; i++) {
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
                  employeeScope.managerEmpId = extractId[extractId.length - 1]
            }
        }

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

