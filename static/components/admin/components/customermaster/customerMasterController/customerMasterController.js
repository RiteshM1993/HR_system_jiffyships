angular.module('adminApp.customerMasterController',[])

.controller('customerMasterController',['customerMasterService','$stateParams','$state','$http','$rootScope', function(customerMasterService,$stateParams,$state,$http,$rootScope){

    var customerMasterScope = this;


    // Save Function

    customerMasterScope.saveCustomerMaster = function(){

      var startDate = customerMasterScope.startDate.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");

        CustomerMasterData={
            'CustomerName' : customerMasterScope.customer_name ,
            'CustomerAddress' : customerMasterScope.customer_address,
            'startDate' : startDate,
            'ContactPersonName':customerMasterScope.contact_person_name,
            'ContactPersonEmailid':customerMasterScope.contact_person_emailid,
            'active' : customerMasterScope.active,

        }

        console.log(CustomerMasterData)

        var success = function(response){

            customerMasterScope.successmsg = true
            customerMasterScope.errormsg = false
            console.log(response)
            console.log('success')

        }

        var failure = function(response){
            customerMasterScope.successmsg = false
            customerMasterScope.errormsg = true
            console.log(response)
            console.log('success')

        }

      customerMasterService.saveCustomerMaster(CustomerMasterData, success, failure)

   }


   customerMasterScope.GetCustomerlist = function(){

        $rootScope.checkSession()
        var success = function(response){
            customerMasterScope.listdata = response.data.data
            console.log(customerMasterScope.listdata)
            console.log('success')

        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        customerMasterService.listcustomer(success, failure)
    }

    //    change state with id

    customerMasterScope.changeState = function(customer_id){
        $state.go('editcustomermaster',{
            'obj' : customer_id
        })
    }

    customerMasterScope.geteditcustomer = function(){

        $rootScope.checkSession()

        var id = $stateParams.obj
         var success = function(response){
                console.log('success')
                console.log(response.data.data)
                customerMasterScope.data = response.data.data
            }

            var failure = function(response){
                console.log('failure')
                console.log(response)
            }

            customerMasterService.geteditcustomer(id,success, failure)
    }

     customerMasterScope.updateCustomer = function(){

       var start_date = customerMasterScope.data.start_date.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");

        customerData={
            'id' : customerMasterScope.data.customer_id,
            'customer_name' : customerMasterScope.data.customer_name,
            'customer_address' : customerMasterScope.data.customer_address,
            'start_date': start_date,
            'contact_person_emailid':customerMasterScope.data.contact_person_emailid,
            'contact_person_name' : customerMasterScope.data.contact_person_name,
            'active' : customerMasterScope.data.active,
        }

        console.log(customerData)

        var success = function(response){
            customerMasterScope.successmsg = true
            customerMasterScope.errormsg = false
            console.log(response)
            console.log('success')

        }

        var failure = function(response){
            customerMasterScope.successmsg = false
            customerMasterScope.errormsg = true
            console.log(response)
            console.log('failure')
        }


        customerMasterService.updateCustomer(customerData, success, failure)


    }


    customerMasterScope.stateViewProject = function(id){
         $state.go('stateViewProject',{'obj' : id})
    }

   customerMasterScope.getCustomerProject = function(){

        $rootScope.checkSession()

        var id = $stateParams.obj

        var success = function(response){
            console.log('success')
            console.log(response)
            customerMasterScope.listdata = response.data.data
        }

        var failure = function(response){
            console.log('failure')
            console.log(response)
        }

        customerMasterService.getCustomerProject(id,success, failure)
   }

   customerMasterScope.changeViewPOstate= function(id){
       $state.go('viewcustomerpostate',{'obj' : id})
   }

   customerMasterScope.getCustomerProjectpo = function(){

        $rootScope.checkSession()

        var id = $stateParams.obj

        var success = function(response){
            console.log('success')
            console.log(response)
            customerMasterScope.listdata = response.data.data
        }

        var failure = function(response){
            console.log('failure')
            console.log(response)
        }

        customerMasterService.getCustomerProjectpo(id,success, failure)
   }




     return customerMasterScope;

}])