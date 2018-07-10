angular.module('adminApp.projectAssignController',[])
.controller('projectAssignController',['projectAssignService','$state','$stateParams','$state','$rootScope', function(projectAssignService,$state,$stateParams,$state,$rootScope){
    var projectAssignScope = this;

    projectAssignScope.listProjectManager = function(){

        $rootScope.checkSession()

        var success = function(response){
            console.log('success')
            console.log(response)
            projectAssignScope.projectManager = response.data.data
        }

        var failure = function(response){
            console.log('failure')
            console.log(response)
        }

        projectAssignService.listingProjectManager(success, failure)
    }

    projectAssignScope.showResources = function(projectId){
        $state.go('viewresource',{
            'obj': projectId,
        })
    }

    projectAssignScope.getResouces = function(){
        $rootScope.checkSession()
        var id = $stateParams.obj
        console.log(id)

        var success = function(response){
            console.log('success')
            console.log(response)
            projectAssignScope.resourceData = response.data.data
        }

        var failure = function(response){
            console.log('failure')
            console.log(response)
        }

        projectAssignService.getResource(id, success, failure)

    }


    projectAssignScope.showDocuments = function (projectId){
        $state.go('viewdocuments',{
            'obj': projectId,
        })
    }


    projectAssignScope.getDocuments = function(){
        $rootScope.checkSession()
        var id = $stateParams.obj
        console.log(id)

        var success = function(response){
            console.log('success')
            console.log(response)
            projectAssignScope.projectDoc = response.data.data
        }

        var failure = function(response){
            console.log('failure')
            console.log(response)
        }

        projectAssignService.getDocuments(id, success, failure)

    }

     projectAssignScope.listProjectManagerempassigned = function(){

        $rootScope.checkSession()

        var id = $stateParams.obj

        var success = function(response){
            console.log('success')
            console.log(response.data.data)
            projectAssignScope.projectdata = response.data.data
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        projectAssignService.listProjectManagerEmpAssigned(id, success, failure)
    }




    return projectAssignScope;

}])