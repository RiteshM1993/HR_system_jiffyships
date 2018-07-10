angular.module('adminApp.currencyMasterService',[])

.service('currencyMasterService',['$http', function($http){

    var currencyMaster = {}

    currencyMaster.addCurrency = function(currencyName, currencyLogo, success, failure){
        console.log('hello')
        $http.post('api/addcurrency/',{
            'currencyName' : currencyName,
            'currencyLogo' : currencyLogo,
        }).then(success, failure)
    }

    currencyMaster.listCurrency = function(success, failure){
         $http.get('api/listcurrency/').then(success, failure)
    }

    currencyMaster.delcurrency = function(id, success, failure){
        $http.delete('api/delcurrency/?id='+id).then(success, failure)
    }

    currencyMaster.geteditdata = function(id, success, failure){
        $http.get('api/geteditcurrencydata/?id='+id).then(success, failure)
    }

    currencyMaster.updateCurrency = function(id, currencyName, currencyLogo, success, failure){
         $http.post('api/updatecurrency/',{
            'id': id,
            'currencyName' : currencyName,
            'currencyLogo' : currencyLogo,
        }).then(success, failure)
    }

    return currencyMaster

}])