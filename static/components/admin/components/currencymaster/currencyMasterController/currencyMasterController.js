angular.module('adminApp.currencyMasterController',[])

.controller('currencyMasterController',['currencyMasterService','$stateParams','$state','$rootScope', function(currencyMasterService, $stateParams, $state,$rootScope){

    var currencyMasterScope = this

    currencyMasterScope.addCurrencyMaster = function(){
        var currencyName = currencyMasterScope.currencyname
        var currencyLogo = currencyMasterScope.currenyLogo
       console.log(currencyLogo)
        var success = function(response){
            console.log(response)
            console.log('success')
            currencyMasterScope.successmsg = true
            currencyMasterScope.errormsg = false
        }


        var failure = function(response){
            console.log(response)
            console.log('failure')
            currencyMasterScope.successmsg = false
            currencyMasterScope.errormsg = true
        }

        currencyMasterService.addCurrency(currencyName, currencyLogo, success, failure)

    }

    currencyMasterScope.listCurrencyMaster = function(){
        $rootScope.checkSession()
        var success = function(response){
            console.log(response)
            console.log('success')
            currencyMasterScope.currency = response.data.data
        }


        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        currencyMasterService.listCurrency(success, failure)
    }

    currencyMasterScope.deletecurrency = function(id, $index){

        if (confirm('Are You Sure?')){

            var rowindex = $index

            var success = function(response){
                console.log(response.data.data)
                console.log('success')

                if(response.data.data.response == "success"){
                    currencyMasterScope.currency.splice(rowindex,1)
                }
            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            currencyMasterService.delcurrency(id, success, failure)

        }

    }

    currencyMasterScope.changeState = function(id){
        $state.go('updatecurrencymaster',{
            'obj': id,
        })
    }

    currencyMasterScope.populatedata = function(){

        $rootScope.checkSession()

        var id = $stateParams.obj

        var success = function(response){
            console.log('success')
            currencyMasterScope.data = response.data.data
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        currencyMasterService.geteditdata(id, success, failure)

    }

    currencyMasterScope.updateCurrencyMaster = function(){

        var id = currencyMasterScope.data.currency_id
        var currencyName = currencyMasterScope.data.currency_name
        var currencyLogo = currencyMasterScope.data.currency_logo

        var success = function(response){
            console.log(response)
            console.log('success')
            currencyMasterScope.successmsg = true
            currencyMasterScope.errormsg = false
        }


        var failure = function(response){
            console.log(response)
            console.log('failure')
            currencyMasterScope.successmsg = false
            currencyMasterScope.errormsg = true
        }

        currencyMasterService.updateCurrency(id, currencyName, currencyLogo, success, failure)
    }


    currencyMasterScope.clearForm = function(){
        currencyMasterScope.data.currency_name = ""
        currencyMasterScope.data.currency_logo = ""

    }

    return currencyMasterScope


}])