angular.module('adminApp.projectmasterController',[])

.controller('projectmasterController',['projectmasterService','$stateParams','$state','$http','$rootScope', function(projectmasterService,$stateParams,$state,$http,$rootScope){

    var projectmasterScope = this;

    projectmasterScope.getvalues = function(){

        $rootScope.checkSession()

        getProjecTypemasteridValues = function(){

            var success = function(response){
                projectmasterScope.ProjecTypeMasterValue = response.data.data
            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            projectmasterService.Projecttypemastervalue(success, failure)

        }
        getProjecTypemasteridValues()

        getBusinessUnitValues = function(){

            var success = function(response){
                projectmasterScope.businessUnitValue= response.data.data
            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            projectmasterService.ProjectBusinessUnitValues(success, failure)
        }

        getBusinessUnitValues()

        getCustomerValues = function(){

            var success = function(response){
                projectmasterScope.Customervalues= response.data.data
            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            projectmasterService.Customervalues(success, failure)
        }

        getCustomerValues()

    }


    // Save Function

    projectmasterScope.saveProjectmaster = function(){

      var startDate = projectmasterScope.startDate.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");
      var endDate = projectmasterScope.endDate.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");

        ProjectMasterData={
            'customerId' : projectmasterScope.customerId ,
            'projectName' : projectmasterScope.project_name ,
            'projecttypeMasterid' : projectmasterScope.proj_typemaster_id,
            'startDate' : startDate,
            'endDate' : endDate,
            'resourceCount':projectmasterScope.resource_count,
            'businessUNitid':projectmasterScope. businessunit_id,
            'emp_id' : projectmasterScope.emp_id,
//            'projcurr' : projectmasterScope.projcurr,
//            'projBillRate' : projectmasterScope.projBillRate,
            'projectCost' : projectmasterScope.projectCost,
        }

        console.log(ProjectMasterData)

        var success = function(response){

            projectmasterScope.successmsg = true
            projectmasterScope.errormsg = false
            console.log(response)
            console.log('success')

        }

        var failure = function(response){
            projectmasterScope.successmsg = false
            projectmasterScope.errormsg = true
            console.log(response)
            console.log('success')

        }

      projectmasterService.saveProjectmaster(ProjectMasterData, success, failure)

}

// Listing Function

    projectmasterScope.getProjectMasterlist = function(){

        $rootScope.checkSession()
        var success = function(response){
            projectmasterScope.listdata = response.data.data
            console.log(projectmasterScope.listdata)
            console.log('success')

        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        projectmasterService.listProjectMaster(success, failure)
    }

     // Delete Function

    projectmasterScope.deleteeprojectmaster = function(project_id, $index){

        if (confirm('Are You Sure?')){

            var rowindex = $index

            var success = function(response){
                console.log(response.data.data)
                console.log('success')

                if(response.data.data.response == "success"){
                    projectmasterScope.listdata.splice(rowindex,1)
                }
            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            projectmasterService.deleteeprojectmaster(project_id, success, failure)

        }

    }

    //    change state with id

    projectmasterScope.changeState = function(id){
        $state.go('editprojectmaster',{obj: JSON.stringify(id)})
    }

// insert data into fields function

    projectmasterScope.insertdatarow = function(){

        $rootScope.checkSession()

        id = $stateParams.obj


        var success = function(response){
            console.log('success')
            projectmasterScope.getvalues()

            projectmasterScope.data = response.data.data
            projectmasterScope.emp_id = projectmasterScope.data.emp_id
            console.log(projectmasterScope.data)
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        projectmasterService.geteditdata(id, success, failure)

    }

     // save updated data function
    projectmasterScope.updateprojectmaster = function(){

       var start_date = projectmasterScope.data.start_date.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");
       var end_date = projectmasterScope.data.end_date.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");


        ProjData={
            'id' : projectmasterScope.data.project_id,
            'project_name' : projectmasterScope.data.project_name,
            'proj_typemaster_id' : projectmasterScope.data.proj_typemaster_id,
            'start_date': start_date,
            'end_date' :end_date,
            'resource_count':projectmasterScope.data.resource_count,
            'businessunit_id':projectmasterScope.data.businessunit_id,
            'emp_name' : projectmasterScope.emp_id,
            'customer_id':projectmasterScope.data.customer_id,
//            'currency_name' : projectmasterScope.data.currency_name,
//            'rate_per_hour' : projectmasterScope.data.rate_per_hour,
            'project_cost': projectmasterScope.data.project_cost,

        }

        console.log(ProjData)

        var success = function(response){
            projectmasterScope.successmsg = true
            projectmasterScope.errormsg = false
            console.log(response)
            console.log('success')

        }

        var failure = function(response){
            projectmasterScope.successmsg = false
            projectmasterScope.errormsg = true
            console.log(response)
            console.log('failure')
        }

        projectmasterService.updateprojectmaster(ProjData, success, failure)
    }


     projectmasterScope.autoCompleteOptions = {

            minimumChars: 1,
            data: function (searchText) {
            searchName= angular.lowercase(searchText)
                return $http.get('/dashboard/api/managernamevalues/?name='+searchName)
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
                  projectmasterScope.emp_id = extractId[extractId.length - 1]
            }
        }


        projectmasterScope.checkErr = function(startDate,endDate) {
            projectmasterScope.errMessage = '';
            var curDate = new Date();

            if(new Date(startDate) < new Date(endDate)){

                projectmasterScope.errMessage = true
                projectmasterScope.error_msg = false

              return false;
            }

             if(new Date(startDate) > new Date(endDate)){
                  projectmasterScope.errMessage = false
                  projectmasterScope.error_msg = true
               return false;

           }

        };


//Purchase Order

    projectmasterScope.changeViewPOstate = function(id){
        $state.go('changeViewPOstate',{obj: id})
    }

    projectmasterScope.getProjectPO= function(){

        $rootScope.checkSession()

        id = $stateParams.obj


        var success = function(response){
            console.log('success')

            projectmasterScope.listdata = response.data.data

            console.log(projectmasterScope.data)
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        projectmasterService.getProjectPO(id, success, failure)

    }



    return projectmasterScope;


}])