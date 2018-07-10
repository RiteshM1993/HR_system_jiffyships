angular.module('loginApp',[])

.controller('loginController',['$scope','$http', function($scope,$http){



    $scope.userlogin = function(){

       var emailid =  $scope.emailid
       // console.log(emailid)
       var success = function(response){

            $scope.successmsg = true
            $scope.errormsg = false
            console.log(response)
            console.log('success')
            if (response.data){

               window.location="/dashboard/";


            }
        }

        var failure = function(response){

            $scope.successmsg = false
            $scope.errormsg = true
            console.log(response)
            console.log('failure')
        }

        $http.post('api/userlogin/',{
            'emailid' : emailid,

        }).then(success, failure)

    }

//      $scope.checkSession = function(){
//
//
//      var success = function(response){
//         checkSession = response.data.data
//         console.log(checkSession)
//         console.log('success')
//     }
//
//      var failure = function(response){
//
//            console.log(response)
//            console.log('failure')
//        }
//
//        $http.get('dashboard/api/checksession/',{
//        }).then(success, failure)
//
//
// }



}])
