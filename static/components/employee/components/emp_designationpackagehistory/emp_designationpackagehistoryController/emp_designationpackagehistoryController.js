angular.module('employeeApp.emp_designationpackagehistoryController',[])
.controller('empdesigpackhistoryController',['$state','$stateParams','empdesigpackhistoryService','$http','$rootScope', function($state, $stateParams, empdesigpackhistoryService,$http,$rootScope){

    var empdesigpackhistoryScope = this

// get values for add page starts
    empdesigpackhistoryScope.getvalues = function(){

        $rootScope.checkSession()

        getdesignation = function(){

            var success = function(response){
                console.log(response.data.data)
                empdesigpackhistoryScope.designation = response.data.data
            }

            var failure = function(response){

                console.log('failure')
            }

            empdesigpackhistoryService.getDesignation(success, failure)
        }

        getdesignation()

        getcurrency = function(){

            var success = function(response){
                console.log(response.data.data)
                empdesigpackhistoryScope.currency = response.data.data
            }

            var failure = function(response){

                console.log('failure')
            }

            empdesigpackhistoryService.getCurrency(success, failure)

        }
        getcurrency()
    }

// get values for add page ends

    empdesigpackhistoryScope.saveEmployeeHistory = function(){

       var fromDate = empdesigpackhistoryScope.fromdate.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");

        data = {
            'emp_id' : empdesigpackhistoryScope.managerEmpId ,
            'salary' : empdesigpackhistoryScope.salary,
            'from_date' : fromDate,
            'active' : empdesigpackhistoryScope.active,
            'currency_id' : empdesigpackhistoryScope.currencyid,
            'designation_id' : empdesigpackhistoryScope.designationid,
        }

        console.log(data)

        var success = function(response){
            empdesigpackhistoryScope.successmsg = true
            empdesigpackhistoryScope.errormsg = false
        }

        var failure = function(response){
            empdesigpackhistoryScope.successmsg = false
            empdesigpackhistoryScope.errormsg = true
            console.log(response)
            console.log('failure')
        }

        empdesigpackhistoryService.saveempdesigpackhistory(data, success, failure)

    }

    empdesigpackhistoryScope.getEmpDesigPackHistoryData = function(){
        id = $stateParams.obj
        $rootScope.checkSession()
        var success = function(response){

            console.log(response.data.data)
            empdesigpackhistoryScope.data = response.data.data
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        empdesigpackhistoryService.listempdesigpackhistory(id,success, failure)
    }

    empdesigpackhistoryScope.deleteEmployeeHistory = function(pckg_id, $index){

        if(confirm('Are You Sure?')){

            var success = function(response){
                console.log(response.data.data)
                empdesigpackhistoryScope.data.splice($index,1)
            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            empdesigpackhistoryService.delEmployeeHistory(pckg_id,success, failure)
        }
    }

    empdesigpackhistoryScope.changetoeditState = function(pckg_id){
        console.log('hi')
        $state.go('editempdesig_pack_history',{
            'obj': pckg_id,
        })
    }

    empdesigpackhistoryScope.populateEditData = function(){

        $rootScope.checkSession()

        id = $stateParams.obj

        var success = function(response){
            console.log(response.data)
            empdesigpackhistoryScope.getvalues()
            empdesigpackhistoryScope.emp_id = response.data.data[0].emp_id
            empdesigpackhistoryScope.data = response.data.data[0]
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        empdesigpackhistoryService.getpopulateEditData(id,success, failure)
    }

    empdesigpackhistoryScope.updateEditData = function(){

       var fromDate = empdesigpackhistoryScope.data.from_date.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");
//       var toDate = empdesigpackhistoryScope.data.to_date.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");

       var extractId = empdesigpackhistoryScope.data.emp_name.split(" ")

       var empId = parseInt(extractId[extractId.length - 1])

       if (isNaN(empId)){
            console.log(empId)
       }
       else{
            empdesigpackhistoryScope.emp_id = empId
       }

        data = {
            'empdesigpack_id': empdesigpackhistoryScope.data.pckg_id,
            'emp_id' : empdesigpackhistoryScope.emp_id,
            'salary' : empdesigpackhistoryScope.data.salary,
            'from_date' : fromDate,
//            'to_date' : toDate,
            'active' : empdesigpackhistoryScope.data.active,
            'currency_id' : empdesigpackhistoryScope.data.currencyid,
            'designation_id' : empdesigpackhistoryScope.data.designationId,
        }


        var success = function(response){

            empdesigpackhistoryScope.successmsg = true
            empdesigpackhistoryScope.errormsg = false
        }

        var failure = function(response){
            empdesigpackhistoryScope.successmsg = false
            empdesigpackhistoryScope.errormsg = true
            console.log(response)
            console.log('failure')
        }
        console.log(data)
        empdesigpackhistoryService.updateempdesigpackhistory(data, success, failure)

    }


    //    auto complete manager
        empdesigpackhistoryScope.autoCompleteOptions = {
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
                  empdesigpackhistoryScope.managerEmpId = extractId[extractId.length - 1]
            }
        }

    empdesigpackhistoryScope.clearform = function(){
        empdesigpackhistoryScope.data.active = ""
        empdesigpackhistoryScope.data.currencyid = ""
        empdesigpackhistoryScope.data.designationId = ""
    }

    return empdesigpackhistoryScope

}])