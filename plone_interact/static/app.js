
/* Copyright (c) 2013 Enfold Systems, Inc. All rights reserved. */


jQuery(function ($) {

    $('#plone-interact-overlay').overlay({
    });

    $('#user-name').click(function (evt) {
        $('#plone-interact-overlay').overlay().load();
        return false;
    });


    $('.plone-interact-close').click(function (evt) {
        $('#plone-interact-overlay').overlay().close();
        return false;
    });

});

0
angular.module('chat', ['firebase']).
controller('Chat', ['$scope', '$timeout', 'angularFireCollection',
    function($scope, $timeout, angularFireCollection) {

        var url = jQuery('meta[name="plone-interact-firebase-url"]').attr('content');
        var authToken = jQuery('meta[name="plone-interact-auth-token"]').attr('content');

        // Log me in.
        var dataRef = new Firebase(url);

        dataRef.auth(authToken, function(error, result) {
            if(error) {
                throw new Error("Login Failed! \n" + error);
            } else {
                var auth = result.auth;
                ploneUsername = auth.ploneUsername;
                if (ploneUsername == 'Anonymous') {
                    $scope.username = 'Anonymous' + Math.floor(Math.random()*101);
                } else {
                    $scope.username = ploneUsername;
                }

                var el = document.getElementById("messagesDiv");
                $scope.messages = angularFireCollection(url, function() {
                    $timeout(function() { el.scrollTop = el.scrollHeight; });
                });

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
