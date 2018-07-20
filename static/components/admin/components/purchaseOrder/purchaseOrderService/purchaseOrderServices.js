angular.module('adminApp.purchaseOrderService',[])

.service('purchaseOrderService',['$http', function($http){

    var purchaseOrder ={};

    purchaseOrder.getBillingType = function(success, failure){
        $http.get('api/listprojecttype/').then(success, failure)
    }

    purchaseOrder.getPoCurrency = function(success, failure){
        $http.get('api/listcurrency/').then(success, failure)
    }

    purchaseOrder.getProjectName = function(success, failure){
        $http.get('api/listprojectmaster/').then(success, failure)
    }

    purchaseOrder.savePurchaseOrder = function(dataobj,success, failure){

        $http.post('api/savepurchaseorder/',{
            'projectName' : dataobj.projectName,
            'purchaseOrderNumber' : dataobj.purchaseOrderNumber,
            'startDate' : dataobj.startDate,
            'endDate' : dataobj.endDate,
//            'purchaseOrderResources' : dataobj.purchaseOrderResources,
//            'billingType' : dataobj.billingType,
            'purchaseOrderAmount': dataobj.purchaseOrderAmount,
            'purchaseordercurrency' : dataobj.purchaseordercurrency,
//            'projBillRate' : dataobj.projBillRate,
//            'projectCost' : dataobj.projectCost,

        }).then(success, failure)
    }



    purchaseOrder.getPoData = function(success, failure){
        $http.get('api/listpo/').then(success, failure)
    }

    purchaseOrder.delPoData = function(po_id,success, failure){
        $http.delete('api/delpodata/?id='+po_id).then(success, failure)
    }

    purchaseOrder.getpoeditdata = function(id, success, failure){
        $http.get('api/poeditdata/?id='+id).then(success, failure)
    }

    purchaseOrder.updatePo = function(PoData, success, failure){

         $http.post('api/updatepo/',{
            'id': PoData.po_id,
            'projectId' : PoData.projectId,
            'poNumber' : PoData.poNumber,
            'startDate' : PoData.startDate,
            'endDate' : PoData.endDate,
//            'resourceCount' : PoData.resourceCount,
//            'billingType' : PoData.billingType,
            'poAmount': PoData.poAmount,
            'currencyId' : PoData.currencyId,
//            'billperhour' : PoData.billperhour,
//            'projectCost' : PoData.projectCost,

        }).then(success, failure)

    }

    purchaseOrder.SavepaymentDetails = function(PayDetails,success,failure){


        $http.post('api/savepopayment/',{

           'id':PayDetails.po_id,
           'CheckTransactionDetails': PayDetails.CheckTransactionDetails,
           'receiveddate': PayDetails.receiveddate,
           'Description':PayDetails.Description,
        }).then(success,failure)

    }

    purchaseOrder.paymentdetails = function(success, failure){
        $http.get('api/getpoPayment/').then(success, failure)
    }

    return purchaseOrder;
}])

