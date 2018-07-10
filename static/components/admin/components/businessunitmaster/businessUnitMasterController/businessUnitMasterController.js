angular.module('adminApp.businessUnitMasterController',[])
.controller('businessUnitMasterController',['businessUnitMasterService', '$stateParams','$state','$scope','$http','$rootScope', function(businessUnitMasterService, $stateParams, $state, $scope,$http,$rootScope){

    var businessUnitMasterScope = this;

    businessUnitMasterScope.getBusinessParent = function(){
        $rootScope.checkSession()
        businessUnitMasterScope.listbusinessUnitMaster()
    }

                                                                                                                                                                                                                                                                                        businessUnitMasterScope.managerNamelist=[]
    var empIdList = []

    var getMangeridName = function(){

        var NameEmail = businessUnitMasterScope.managerIdName

        empIdList.push(businessUnitMasterScope.managerEmpId)

        businessUnitMasterScope.managerNamelist.push (NameEmail[0]+' '+NameEmail[1]+' '+NameEmail[2])

        businessUnitMasterScope.managerNameDisplay = businessUnitMasterScope.managerNamelist

    }

    businessUnitMasterScope.removeNameChip = function(index){
        businessUnitMasterScope.managerNameDisplay.splice(index,1)
        empIdList.splice(index,1)
        console.log(empIdList)
    }




    businessUnitMasterScope.addbusinessUnitMaster = function(){

        var data = {
            'businessUnitName' : businessUnitMasterScope.businessunitname,
            'businessParent' : businessUnitMasterScope.businessparent,
            'status' : businessUnitMasterScope.status,
            'managerId' : empIdList,
        }

        var success = function(response){
            console.log(response)
            console.log('success')
            businessUnitMasterScope.successmsg = true
            businessUnitMasterScope.errormsg = false
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
            businessUnitMasterScope.successmsg = false
            businessUnitMasterScope.errormsg = true
        }

        businessUnitMasterService.addBusinessUnit(data, success, failure)

    }

    businessUnitMasterScope.listbusinessUnitMaster = function(){

        $rootScope.checkSession()

        var success = function(response){
//            console.log(response.data.mess)
            console.log(response.data.data)
            console.log('success')
            businessUnitMasterScope.businessUnit = response.data.data

            $scope.currentPage = 0;

              $scope.paging = {
                total: 100,
                current: 1,
                onPageChanged: loadPages,
              };

              function loadPages() {
                console.log('Current page is : ' + $scope.paging.current);

                // TODO : Load current page Data here

                $scope.currentPage = response.data.data;
              }
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        businessUnitMasterService.listBusinessUnit(success, failure)
    }

    businessUnitMasterScope.deleteBusinessUnit = function(business_id, $index){

        if (confirm('Are You Sure?')){

            var rowindex = $index

            var success = function(response){
                console.log(response.data.data)
                console.log('success')

                if(response.data.data.response == "success"){
                    businessUnitMasterScope.businessUnit.splice(rowindex,1)
                }
            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            var id = business_id

            businessUnitMasterService.delBusinessUnit(id, success, failure)

        }

    }

    businessUnitMasterScope.changeState = function(business_id){
        id = business_id
        $state.go('editbusinessunit',{
            'obj' : id,
        })
    }

//    populate data in fields
    businessUnitMasterScope.populateData = function(){
        $rootScope.checkSession()
        businessUnitMasterScope.listbusinessUnitMaster()
        id = $stateParams.obj

        var success = function(response){
            console.log('success')
            console.log(response.data.data)
            businessUnitMasterScope.data = response.data.data
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        businessUnitMasterService.geteditdata(id, success, failure)

    }

// update data to db
    businessUnitMasterScope.updatebusinessUnitMaster = function(){
        var data = {
            'id' : businessUnitMasterScope.data.business_id,
            'businessUnitName' : businessUnitMasterScope.data.business_name,
            'businessParent' : businessUnitMasterScope.data.business_parent,
            'status' : businessUnitMasterScope.data.status,
            'managerId' : empIdList,

        }

        var success = function(response){
            console.log(response)
            console.log('success')
            businessUnitMasterScope.successmsg = true
            businessUnitMasterScope.errormsg = false
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
            businessUnitMasterScope.successmsg = false
            businessUnitMasterScope.errormsg = true
        }


        businessUnitMasterService.updateBusinessUnit(data, success, failure)
    }


    //    auto complete manager
        businessUnitMasterScope.autoCompleteOptions = {
            minimumChars: 1,
            data: function (searchText) {
                searchName =angular.lowercase(searchText)
                return $http.get('/employee/api/listmanagerename/?name='+searchName)
                    .then(function (response) {
                        var data = response.data.data
                        dataobj = []
                        for (i = 0; i < data.length; i++) {
                           dataobj.push({
                               'empName_email': data[i].emp_name+' ('+data[i].email_id+') '+data[i].emp_id,
                           })
                        }

                        return _.map(dataobj, 'empName_email');

                    });
            },

            itemSelected: function (e) {
                  var extractId = e.item.split(" ")
                  businessUnitMasterScope.managerIdName=e.item.split(" ")
                  businessUnitMasterScope.managerEmpId = extractId[extractId.length - 1]
                  getMangeridName()
            }
        }


        businessUnitMasterScope.clearForm = function(){
            businessUnitMasterScope.managerNameDisplay = ""
            businessUnitMasterScope.data.business_parent = ""
            businessUnitMasterScope.data.status = ""
        }








    return businessUnitMasterScope;

}])