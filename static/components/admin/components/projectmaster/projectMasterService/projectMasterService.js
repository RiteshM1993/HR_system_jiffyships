angular.module('adminApp.projectmasterService',[])

.service('projectmasterService',['$http', function($http){

    var projectmaster ={};

     projectmaster.Projecttypemastervalue = function(success, failure){
        $http.get('/dashboard/api/projectmastervalues/').then(success, failure)
     }

      projectmaster.ProjectBusinessUnitValues = function(success, failure){
        $http.get('/dashboard/api/projectbusinessunitvalues/').then(success, failure)
     }

     projectmaster.Customervalues = function(success, failure){
        $http.get('/dashboard/api/customervalues/').then(success, failure)
     }




     projectmaster.saveProjectmaster = function(ProjectMasterData, success, failure){

        $http.post('api/saveprojectmaster/',{
            'customerId' : ProjectMasterData.customerId,
            'projectName' : ProjectMasterData.projectName,
            'projecttypeMasterid' : ProjectMasterData.projecttypeMasterid,
            'startDate' : ProjectMasterData.startDate,
            'endDate' : ProjectMasterData.endDate,
            'resourceCount' : ProjectMasterData.resourceCount,
            'businessUNitid' : ProjectMasterData.businessUNitid,
            'emp_id': ProjectMasterData.emp_id,
            'projectCost':ProjectMasterData.projectCost,

        }).then(success, failure)
    }


    projectmaster.listProjectMaster = function(success, failure){
        $http.get('api/listprojectmaster/').then(success, failure)
    }

    projectmaster.deleteeprojectmaster = function(project_id, success, failure){
        $http.delete('api/deleteeprojectmaster/?id='+project_id).then(success, failure)
    }

    projectmaster.geteditdata = function(id, success, failure){
        $http.get('api/geteditprojectmaster/?id='+id).then(success, failure)
    }

    projectmaster.updateprojectmaster = function(ProjData, success, failure){

        $http.post('api/updateeprojectmaster/',{
            'customer_id': ProjData.customer_id,
            'id' : ProjData.id,
            'projectName' : ProjData.project_name,
            'projecttypeMasterid' : ProjData.proj_typemaster_id,
            'start_date': ProjData.start_date,
            'end_date' :ProjData.end_date,
            'resourceCount':ProjData.resource_count,
            'businessUNitid':ProjData.businessunit_id,
            'emp_id': ProjData.emp_name,
            'projectCost':ProjData.project_cost

        }).then(success, failure)
    }


    projectmaster.getProjectPO = function(id, success, failure){
        $http.get('api/getprojectpo/?id='+id).then(success, failure)
    }

     return projectmaster;

}])