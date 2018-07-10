angular.module('adminApp.billingService',[])

.service('billingService',['$http', function($http){

    var billing ={};


      billing.saveBilling = function(billData, success, failure){
//        console.log(ProjectMasterData)
        $http.post('api/savebilling/',{
            'project_id' : billData.project_id,
            'startDate' : billData.startDate,
            'endDate' : billData.endDate,
            'billresourceCount' : billData.billresourceCount,
            'totalBill' : billData.totalBill,


        }).then(success, failure)
    }


    billing.getBillinglist = function(success, failure){
        $http.get('/dashboard/api/listbilling/').then(success, failure)
    }

    billing.generateBillinglist = function(success, failure){
        $http.get('/dashboard/api/generatebilling/').then(success, failure)
    }
    return billing;

}])

