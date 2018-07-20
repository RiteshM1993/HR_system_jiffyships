angular.module('adminApp.purchaseOrderController',[])

.controller('purchaseOrderController',['purchaseOrderService','$state','$stateParams','$rootScope','$scope', function(purchaseOrderService,$state,$stateParams,$rootScope,$scope){

    var purchaseOrderScope = this;

    $scope.filterPopover = {

     payment:{
       templateUrl:'payment.html',
       title: 'Payment Status',
       value:'',
       reset: function(){
           this.value = '';
       }
     }

   }

    purchaseOrderScope.getValues = function(){

        $rootScope.checkSession()

        getProjectName = function(){
            var success = function(response){
                console.log(response.data.data)
                purchaseOrderScope.projectname = response.data.data
            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            purchaseOrderService.getProjectName(success, failure)
        }

        getBillingType = function(){

            var success = function(response){
                console.log(response.data.data)
                purchaseOrderScope.billingType = response.data.data
            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            purchaseOrderService.getBillingType(success, failure)
        }

        getPoCurrency= function(){

            var success = function(response){
                console.log(response.data.data)
                purchaseOrderScope.poCurrency = response.data.data
            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            purchaseOrderService.getPoCurrency(success, failure)
        }

        getProjectName()

        getPoCurrency()

        getBillingType()
    }


    purchaseOrderScope.savePurchaseOrder = function(){

        var startDate = purchaseOrderScope.startDate.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");
        var endDate = purchaseOrderScope.endDate.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");

        var dataobj = {
            'projectName' : purchaseOrderScope.project_id,
            'purchaseOrderNumber': purchaseOrderScope.purchaseordernumber,
            'startDate' : startDate,
            'endDate' : endDate,
            'purchaseOrderAmount' : purchaseOrderScope.purchaseorderamount,
            'purchaseordercurrency' : purchaseOrderScope.purchaseordercurrency,
        }

        var success = function(response){
            console.log(response.data.data)
            purchaseOrderScope.successmsg = true
            purchaseOrderScope.errormsg = false
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
            purchaseOrderScope.successmsg = false
            purchaseOrderScope.errormsg = true
        }

        purchaseOrderService.savePurchaseOrder(dataobj,success, failure)
    }


    purchaseOrderScope.getPoData = function(){

        $rootScope.checkSession()

        var success = function(response){
            console.log(response.data.data)
            purchaseOrderScope.listdata = response.data.data
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        purchaseOrderService.getPoData(success, failure)
    }


    purchaseOrderScope.deletePo = function(po_id, $index){
        if(confirm('Are You Sure?')){
            var success = function(response){
                console.log(response.data.data)
                purchaseOrderScope.listdata.splice($index,1)
            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            purchaseOrderService.delPoData(po_id,success, failure)

        }

    }

    purchaseOrderScope.changeEditState = function(id){

        $state.go('editpurchaseorder',{obj: id})

    }


    purchaseOrderScope.insertdatarow = function(){

        $rootScope.checkSession()

        var id = $stateParams.obj

        var success = function(response){
            console.log('success')

            purchaseOrderScope.getValues()
            console.log(response.data.data)
//            console.log(typeof(response.data.data.po_project_cost))
            purchaseOrderScope.data = response.data.data
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        purchaseOrderService.getpoeditdata(id, success, failure)

    }

    // save updated data function
    purchaseOrderScope.updatePo= function(){

       var start_date = purchaseOrderScope.data.po_start_date.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");
       var end_date = purchaseOrderScope.data.po_end_date.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");


        PoData={
            'po_id': purchaseOrderScope.data.po_id,
            'projectId': purchaseOrderScope.data.project_id,
            'poNumber': purchaseOrderScope.data.po_number,
            'startDate': start_date,
            'endDate': end_date,
            'poAmount': purchaseOrderScope.data.po_amount,
            'currencyId': purchaseOrderScope.data.po_currency_id,
        }


        var success = function(response){
            purchaseOrderScope.successmsg = true
            purchaseOrderScope.errormsg = false
            console.log(response)
            console.log('success')

        }

        var failure = function(response){
            purchaseOrderScope.successmsg = false
            purchaseOrderScope.errormsg = true
            console.log(response)
            console.log('failure')
        }

        purchaseOrderService.updatePo(PoData, success, failure)
    }


     purchaseOrderScope.changeState = function(id){

        $state.go('paymentdetails', {obj: id})

    }

    purchaseOrderScope.SavePaymentDetails = function(){

       var receiveddate = purchaseOrderScope.receiveddate.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");

       var id = $stateParams.obj



       PayDetails= {

              'po_id':id,
              'CheckTransactionDetails': purchaseOrderScope.CheckTransactionDetails,
              'receiveddate': receiveddate,
              'Description':purchaseOrderScope.Description,
       }

       var success = function(response){
            console.log(response.data.data)
            purchaseOrderScope.successmsg = true
            purchaseOrderScope.errormsg = false
        }

       var failure = function(response){
            console.log(response)
            console.log('failure')
            purchaseOrderScope.successmsg = false
            purchaseOrderScope.errormsg = true
        }

        purchaseOrderService.SavepaymentDetails(PayDetails,success,failure)


    }


    purchaseOrderScope.getPoPaymentData = function(){

        $rootScope.checkSession()

        var success = function(response){
            console.log(response.data.data)
            purchaseOrderScope.listdata = response.data.data
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        purchaseOrderService.paymentdetails(success, failure)
    }




     purchaseOrderScope.checkErr = function(startDate,endDate) {
            purchaseOrderScope.errMessage = '';
            var curDate = new Date();

            if(new Date(startDate) < new Date(endDate)){

                purchaseOrderScope.errMessage = true
                purchaseOrderScope.error_msg = false

              return false;
            }

             if(new Date(startDate) > new Date(endDate)){
                  purchaseOrderScope.errMessage = false
                  purchaseOrderScope.error_msg = true
               return false;
           }
        };

    return purchaseOrderScope;


}])