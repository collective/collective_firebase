
angular.module('chat', ['firebase']).
controller('Chat', ['$scope', '$timeout', 'angularFireCollection',
    function($scope, $timeout, angularFireCollection) {
        var el = document.getElementById("messagesDiv");
        //var url = 'https://green-test-firebase.firebaseio-demo.com/chat';
        var url = 'https://green-test-firebase.firebaseio.com/chat';
        $scope.messages = angularFireCollection(url, function() {
            $timeout(function() { el.scrollTop = el.scrollHeight; });
        });

        //var ploneUsername = jQuery('meta[name="firebaseplonedemo-username"]').attr('content');
        var authToken = jQuery('meta[name="firebaseplonedemo-auth-token"]').attr('content');
        // Log me in.
        var dataRef = new Firebase(url);

        dataRef.auth(authToken, function(error, result) {
            if(error) {
                console.log("Login Failed!", error);
            } else {
                var auth = result.auth;
                ploneUsername = auth.ploneUsername;
                if (ploneUsername == 'Anonymous') {
                    $scope.username = 'Anonymous' + Math.floor(Math.random()*101);
                } else {
                    $scope.username = ploneUsername;
                }
                $scope.addMessage = function() {
                    $scope.messages.add({from: $scope.username, content: $scope.message}, function() {
                        el.scrollTop = el.scrollHeight;
                    });
                    $scope.message = "";

                    // prevent double click warning for this form
                    jQuery('input[value="Send"]').removeClass('submitting');

                };
            }
        });


    }
]);
