angular.module('employeeApp.empDocController',[])

.controller('empDocController',['empDocService','$stateParams','$state','$rootScope', function(empDocService,$stateParams,$state,$rootScope){

    var empDocScope = this;

    empDocScope.saveDoc = function(){

        var formdata = new FormData();

        formdata.append('docName', empDocScope.docname);
        formdata.append('file', empDocScope.empdoc);

        var success = function(response){
            empDocScope.successmsg = true
            empDocScope.errormsg = false
        }

        var failure = function(response){
            empDocScope.successmsg = false
            empDocScope.errormsg = true
            console.log(response)
            console.log('failure')
        }

        empDocService.saveEmpDoc(formdata, success, failure)

    }

    empDocScope.getEmpDoc = function(){

        $rootScope.checkSession()

        var success = function(response){
            console.log(response)
            empDocScope.data=response.data.data
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        empDocService.listEmpDoc(success, failure)
    }


    empDocScope.deleteEmpDoc = function(docId, $index){
        if(confirm('Are you sure?')){

            var success = function(response){
                empDocScope.data.splice($index,1)
            }

            var failure = function(response){
                console.log(response)
                console.log('failure')
            }

            empDocService.delEmpDoc(docId,success, failure)
        }


    }


    empDocScope.changetoeditState = function(docId){
        $state.go('editempdoc',{
            'obj': docId,
        })
    }

    empDocScope.getvalues = function(){

        $rootScope.checkSession()

        var id = $stateParams.obj
        console.log(id)
        var success = function(response){
            console.log(response.data.data)
            empDocScope.data = response.data.data
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        empDocService.geteditEmpDoc(id, success, failure)
    }


    empDocScope.updateDoc = function(){
        var id = empDocScope.data.docId
        var formdata = new FormData();
        formdata.append('id', id);
        formdata.append('docName', empDocScope.data.doc_name);
        formdata.append('file', empDocScope.empdoc);

        var success = function(response){
            empDocScope.successmsg = true
            empDocScope.errormsg = false
        }

        var failure = function(response){
            empDocScope.successmsg = false
            empDocScope.errormsg = true
            console.log(response)
            console.log('failure')
        }

        empDocService.updateEmpDoc(formdata, success, failure)

    }

    return empDocScope;


}])

.directive('fileModel',['$parse', function($parse){
return{
    restrict: 'A',
    link: function(scope,element,attrs){
          var model=$parse(attrs.fileModel);
          var modelSetter = model.assign;

          element.bind('change', function(){
            scope.$apply(function(){
            modelSetter(scope, element[0].files[0]);
               });
          });
       }
    };
 }]);