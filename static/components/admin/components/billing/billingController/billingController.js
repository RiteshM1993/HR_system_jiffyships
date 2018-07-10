angular.module('adminApp.billingController',[])

.controller('billingController',['billingService','$stateParams','$state','$http','$rootScope', function(billingService,$stateParams,$state,$http,$rootScope){


    var billingScope = this;

    billingScope.autoCompleteOptions = {

            minimumChars: 1,
            data: function (searchText) {
            searchName= angular.lowercase(searchText)
            console.log(searchName)
                return $http.get('api/ProjectNameValues/?name='+searchName)
                    .then(function (response) {
                        var data = response.data.data
                        console.log(data)
                        dataobj = []
                        for(i = 0; i < data.length; i++){
                        dataobj.push({
                          'projnameID': data[i].project_name+' '+(data[i].project_id)
                        })
                    }
                        return _.map(dataobj, 'projnameID');
                    });
            },



            itemSelected: function (e) {
                  var extractId = e.item.split(" ")
                  console.log(extractId)
                  console.log(extractId[extractId.length - 1])
                  billingScope.project_id = extractId[extractId.length - 1]
            }
        }

        billingScope.saveBilling = function(){

         var startDate = billingScope.startDate.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");
         var endDate = billingScope.endDate.replace(/(\d\d)\/(\d\d)\/(\d{4})/, "$3-$1-$2");

        billData={
            'project_id' : billingScope.project_id,
            'startDate' : startDate,
            'endDate' : endDate,
            'billresourceCount':billingScope.empcount,
            'totalBill':billingScope.rate_per_hour,

        }

        console.log(billData)

        var success = function(response){

            billingScope.successmsg = true
            billingScope.errormsg = false
            console.log(response)
            console.log('success')

        }

        var failure = function(response){
            billingScope.successmsg = false
            billingScope.errormsg = true
            console.log(response)
            console.log('success')

        }

      billingService.saveBilling(billData, success, failure)

}

   billingScope.getBillinglist = function(){

        $rootScope.checkSession()

        var success = function(response){
            billingScope.listdata = response.data.data
            console.log(billingScope.listdata)
            console.log('success')

        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        billingService.getBillinglist(success, failure)
    }


   billingScope.Generatebill=function(){

      var success = function(response){
            billingScope.empcount = response.data.data[0].empcount
            billingScope.rate_per_hour = response.data.data[0].rate_per_hour
            console.log(response)
            console.log('success')

        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }


        billingService.generateBillinglist(success, failure)
    }



         return billingScope;


}])
