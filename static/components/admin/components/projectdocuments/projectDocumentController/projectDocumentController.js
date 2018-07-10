angular.module('adminApp.projectdocumentController',[])

.controller('projectdocumentController',['projectdocumentService','$stateParams','$state','$http','$rootScope', function(projectdocumentService,$stateParams,$state,$http,$rootScope){

    var projectdocumentScope = this;



    projectdocumentScope.saveProjectDoc = function(){

        var formdata = new FormData();

        formdata.append('project_id', projectdocumentScope.project_id);
        formdata.append('docName', projectdocumentScope.docname);
        formdata.append('docfile', projectdocumentScope.docfile);

        var success = function(response){
            projectdocumentScope.successmsg = true
            projectdocumentScope.errormsg = false
        }

        var failure = function(response){
            projectdocumentScope.successmsg = false
            projectdocumentScope.errormsg = true
            console.log(response)
            console.log('failure')
        }

        projectdocumentService.saveProjectDoc(formdata, success, failure)

    }


    projectdocumentScope.autoCompleteOptions = {

            minimumChars: 1,
            data: function (searchText) {
            searchName= angular.lowercase(searchText)
            console.log(searchName)
                return $http.get('api/projectnamevalues/?name='+searchName)
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
                  projectdocumentScope.project_id = extractId[extractId.length - 1]
            }
        }


        // Listing Function

    projectdocumentScope.getProjectDocumentlist = function(){

        $rootScope.checkSession()

        var success = function(response){
            projectdocumentScope.listdata = response.data.data
            console.log(projectdocumentScope.listdata)
            console.log('success')

        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        projectdocumentService.listProjectDocument(success, failure)
    }

    projectdocumentScope.delProjDoc = function(proj_doc_id, $index){
        if(confirm('Are You Sure?')){

            var success = function(response){
                console.log('success')
                console.log(response)
                if(response.data.data = "success"){
                    projectdocumentScope.listdata.splice(rowindex,1)
                }
            }

            var failure = function(response){
                console.log('failure')
                console.log(response)
            }

            projectdocumentService.delProjDoc(proj_doc_id, success, failure)

        }
    }




//    projectdocumentScope.delProjDoc = function (proj_doc_id, $index){
//
//        if(confirm('Are you sure?')){
//
//            var rowindex = $index
//
//            var success = function(response){
//
//                if(response.data.data.successmsg == "success"){
//                    projectdocumentScope.listdata.splice(rowindex,1)
//                }
//                console.log(response.data.data.successmsg)
//                console.log('success')
//
//            }
//            var failure = function(response){
//
//                console.log(response)
//                console.log('failure')
//
//            }
//
//            projectdocumentService.delProjDoc(proj_doc_id, success, failure)
//        }
//
//    }


    //    change state with id

    projectdocumentScope.changeState = function(id){
        $state.go('editprojectdocument',{obj: JSON.stringify(id)})
    }


    // insert data into fields function

    projectdocumentScope.insertdatarow = function(){

        $rootScope.checkSession()
        id = $stateParams.obj


        var success = function(response){
            console.log('success')

            projectdocumentScope.data = response.data.data
            projectdocumentScope.project_id = projectdocumentScope.data.project_id
            console.log(projectdocumentScope.data)
        }

        var failure = function(response){
            console.log(response)
            console.log('failure')
        }

        projectdocumentService.insertdatarow(id, success, failure)

    }

     projectdocumentScope.updateDoc = function(){
        var id = projectdocumentScope.data.proj_doc_id
        var formdata = new FormData();
        formdata.append('id', id);
        formdata.append('project_name', projectdocumentScope.project_id )
        formdata.append('docName', projectdocumentScope.data.doc_name);
        formdata.append('file', projectdocumentScope.data.docfile);

        var success = function(response){
            projectdocumentScope.successmsg = true
            projectdocumentScope.errormsg = false
        }

        var failure = function(response){
            projectdocumentScope.successmsg = false
            projectdocumentScope.errormsg = true
            console.log(response)
            console.log('failure')
        }

        projectdocumentService.updateProjDoc(formdata, success, failure)

    }


        return projectdocumentScope;


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

