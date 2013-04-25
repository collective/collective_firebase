
/* Copyright (c) 2013 Enfold Systems, Inc. All rights reserved. */



jQuery(function ($) {

    var $overlay = $('#plone-interact-overlay');

    $overlay.overlay({
    });

    // global helper function to show the overlay
    window.showInteractOverlay = function() {
        $overlay.overlay().load();
    };

    //$('#user-name').click(function (evt) {
    //    showInteractOverlay();
    //    return false;
    //});

    $overlay.find('.plone-interact-close').click(function (evt) {
        $overlay.overlay().close();
        return false;
    });

});

var app = angular.module('task', ['firebase']);

app.controller('Task', ['$scope', '$timeout', 'angularFireCollection',
    function($scope, $timeout, angularFireCollection) {

        var url = jQuery('meta[name="plone-interact-firebase-url"]').attr('content');
        var authToken = jQuery('meta[name="plone-interact-auth-token"]').attr('content');

        // Log me in.
        // Each user logs in to /users/<username>/tasks.
        var dataRef = new Firebase(url);

        dataRef.auth(authToken, function(error, result) {
            if(error) {
                throw new Error("Login Failed! \n" + error);
            } else {
                var auth = result.auth;

                if (auth.ploneUsername == 'Anonymous') {
                    $scope.username = 'Anonymous' + Math.floor(Math.random()*101);
                } else {
                    $scope.username = auth.ploneUsername;
                }

                var homeUrl = url + auth.userPrefix + '/tasks';

                var el = document.getElementById("messagesDiv");
                $scope.messages = angularFireCollection(homeUrl, function() {
                    $timeout(function () {
                        el.scrollTop = el.scrollHeight;
                    });
                });

                $scope.addTask = function() {
                    $scope.messages.add({
                        from: $scope.username,
                        content: $scope.message
                    }, function() {
                        el.scrollTop = 0;
                    });
                    $scope.message = "";

                    // prevent double click warning for this form
                    // FIXME to only match inside us
                    jQuery('#plone-interact-overlay input').removeClass('submitting');

                };

                $scope.removeTask = function (task) {
                    $scope.messages.remove(task);
                };

            }
        });

    }
]);
