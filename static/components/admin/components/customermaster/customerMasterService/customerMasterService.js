angular.module('adminApp.customerMasterService',[])

.service('customerMasterService',['$http', function($http){

    var customermaster ={};

     customermaster.saveCustomerMaster = function(CustomerMasterData, success, failure){
//        console.log(ProjectMasterData)
        $http.post('api/savecustomermaster/',{
            'CustomerName' : CustomerMasterData.CustomerName,
            'CustomerAddress' : CustomerMasterData.CustomerAddress,
            'startDate' : CustomerMasterData.startDate,
            'ContactPersonName':CustomerMasterData.ContactPersonName,
            'ContactPersonEmailid':CustomerMasterData.ContactPersonEmailid,
            'active' : CustomerMasterData.active,



        }).then(success, failure)
    }

    customermaster.listcustomer = function(success, failure){
        $http.get('api/listcustomer/').then(success, failure)
    }

    customermaster.geteditcustomer = function(id, success, failure){
        $http.get('api/geteditcustomer/?id='+id).then(success, failure)
    }

    customermaster.updateCustomer = function(customerData, success, failure){

        $http.put('api/updatecustomer/',{
            'id' : customerData.id,
            'customer_name' : customerData.customer_name,
            'customer_address' : customerData.customer_address,
            'start_date': customerData.start_date,
            'contact_person_name':customerData.contact_person_name,
            'contact_person_emailid':customerData.contact_person_emailid,
            'status':customerData.active,

        }).then(success, failure)
    }


    customermaster.getCustomerProject = function(id,success, failure){
        $http.get('api/getcustomerproject/?id='+id).then(success, failure)
    }

    customermaster.getCustomerProjectpo = function(id,success, failure){
        $http.get('api/getcustomerprojectpo/?id='+id).then(success, failure)
    }

    return customermaster;


}])

