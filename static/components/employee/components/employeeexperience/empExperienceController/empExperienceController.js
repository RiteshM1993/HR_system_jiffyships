angular.module('employeeApp.empExperienceController',[])

.controller('empexperienceController',['$state','$stateParams','empexperienceService','$rootScope', function($state,$stateParams,empexperienceService,$rootScope){

    var empExperienceScope = this;

    empExperienceScope.companyrowdata = []

    empExperienceScope.addcompanyrows= function(){

        var fromDate = empExperienceScope.fromdate.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");
        var toDate = empExperienceScope.todate.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");

        data = {
            'prevCompanyName' : empExperienceScope.prevCompanyName,
            'jobTitle' : empExperienceScope.jobTitle,
            'fromDate' : fromDate,
            'toDate' : toDate,
            'jobDescription' : empExperienceScope.jobDescription,
        }

        empExperienceScope.companyrowdata.push(data)

        console.log(empExperienceScope.companyrowdata)
    }

    empExperienceScope.saveEmployeeExperience = function(){

       var data = empExperienceScope.companyrowdata

       console.log(data)

        var success = function(response){
            console.log(response)
            console.log('success')
            empExperienceScope.successmsg = true
            empExperienceScope.errormsg = false
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
            empExperienceScope.successmsg = false
            empExperienceScope.errormsg = true
        }

        empexperienceService.saveEmpExperience(data,success,failure)

    }

    empExperienceScope.getEmpExperience = function(){

       id = $stateParams.obj

        $rootScope.checkSession()

        var success = function(response){
            console.log(response)
            console.log('success')
            empExperienceScope.data = response.data.data
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        empexperienceService.listEmpExperience(id,success,failure)
    }

    empExperienceScope.deleteEmpExperience = function (id, $index){
        if (confirm('Are you sure?')){
                var success = function(response){
                if(response){
                   empExperienceScope.data.splice($index,1)
                }
            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            empexperienceService.delEmpExperience(id,success,failure)
        }
    }

    empExperienceScope.changetoeditState = function(id){

        $state.go('editempexperience',{
            'obj':id,
        })
    }

    empExperienceScope.geteditvalues = function(){

        $rootScope.checkSession()

        var id = $stateParams.obj

        var success = function(response){
            console.log(response)
            console.log('success')
            empExperienceScope.editdata = response.data.data
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        empexperienceService.geteditEmpExperiencedata(id,success,failure)
    }

    empExperienceScope.updateEmployeeExperience = function(){

        var fromDate = empExperienceScope.editdata.from_date.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");
        var toDate = empExperienceScope.editdata.to_date.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");

        data = {
            'id' : empExperienceScope.editdata.emp_expr_id,
            'prevCompanyName' : empExperienceScope.editdata.prev_company_name,
            'jobTitle' : empExperienceScope.editdata.job_title,
            'fromDate' : fromDate,
            'toDate' : toDate,
            'jobDescription' : empExperienceScope.editdata.job_description,
        }

        var success = function(response){
            console.log(response)
            console.log('success')
            empExperienceScope.successmsg = true
            empExperienceScope.errormsg = false
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
            empExperienceScope.successmsg = false
            empExperienceScope.errormsg = true
        }

        empexperienceService.updatedataEmpExperiencedata(data,success,failure)

    }





    return empExperienceScope;

}])