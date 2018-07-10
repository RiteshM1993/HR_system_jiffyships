angular.module('adminApp.projecttypeController',[])

.controller('projecttypeController',['projecttypeService','$state','$stateParams','$rootScope', function(projecttypeService,$state,$stateParams,$rootScope){

    var projecttypeScope = this;

    projecttypeScope.saveProjecttype = function(){

       var projecttypename =  projecttypeScope.projecttypename
        var success = function(response){

            projecttypeScope.successmsg = true
            projecttypeScope.errormsg = false
            console.log(response)
            console.log('success')
        }

        var failure = function(response){

            projecttypeScope.successmsg = false
            projecttypeScope.errormsg = true
            console.log(response)
            console.log('failure')
        }

         projecttypeService.addProjecttype(projecttypename, success, failure)
    }


    // Listing Function

    projecttypeScope.getProjecttypelist = function(){

        $rootScope.checkSession()

        var success = function(response){
            projecttypeScope.listdata = response.data.data
            console.log(projecttypeScope.listdata)
            console.log('success')

        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        projecttypeService.listProjecttype(success, failure)
    }

    // Delete Function


    projecttypeScope.deleteProjecttype = function (proj_id, $index){

        if(confirm('Are you sure?')){

            var rowindex = $index

            var success = function(response){

                if(response.data.data.successmsg == "success"){
                    projecttypeScope.listdata.splice(rowindex,1)
                }
                console.log(response.data.data.successmsg)
                console.log('success')

            }
            var failure = function(response){

                console.log(response)
                console.log('failure')

            }

            projecttypeService.deleteProjecttype(proj_id, success, failure)
        }

    }

    //    change state with id

    projecttypeScope.changeState = function(id){
        $state.go('editprojecttype',{obj: JSON.stringify(id)})
    }

    // insert data into fields function

    projecttypeScope.insertdatarow = function(){

        $rootScope.checkSession()

        id = $stateParams.obj

        listdata = []

        var success = function(response){
            console.log('success')

            listdata.push(response.data.data)

            projecttypeScope.data = listdata
            console.log(projecttypeScope.data)
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        projecttypeService.geteditdata(id, success, failure)

    }
    // save updated data function
    projecttypeScope.updateProjecttype = function(){

         projectData={
            'projid' : projecttypeScope.data[0].proj_id,
            'projName' : projecttypeScope.data[0].proj_name,
        }

        var success = function(response){

            projecttypeScope.successmsg = true
            projecttypeScope.errormsg = false
            console.log(response)
            console.log('success')

        }

        var failure = function(response){

            projecttypeScope.successmsg = false
            projecttypeScope.errormsg = true
            console.log(response)
            console.log('failure')

        }


        projecttypeService.updateProjecttype(projectData, success, failure)

    }

         return projecttypeScope;

}])