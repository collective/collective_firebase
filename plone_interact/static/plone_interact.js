
/* Copyright (c) 2013 Enfold Systems, Inc. All rights reserved. */


jQuery(function ($) {

    var $overlay = $('#noti-overlay');

    $overlay.overlay({
    });

    // global helper function to show the overlay
    window.showInteractOverlay = function() {
        $overlay.overlay().load();
    };

    $('.noti-badge').click(function (evt) {
        showInteractOverlay();
        return false;
    });

    $overlay.find('.noti-close').click(function (evt) {
        $overlay.overlay().close();
        return false;
    });

});

var app = angular.module('task', ['firebase', 'monospaced.elastic']);

app.controller('TaskController', ['$scope', '$timeout', 'angularFireCollection',
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
                var homeUrl = url + auth.userPrefix + '/tasks';
                $scope.username = auth.ploneUserid;

                var el = document.getElementById("noti-messages");
                $scope.messages = angularFireCollection(homeUrl, function() {
                    $timeout(function () {
                        el.scrollTop = el.scrollHeight;
                    });
                });

                $scope.addTask = function() {
                    $scope.messages.add({
                        from: $scope.username,
                        content: $scope.message || '',
                        reason: 'Manually added',
                        ts: new Date().getTime()
                    }, function() {
                        el.scrollTop = 0;
                    });
                    $scope.message = "";
                    // XXX probably a bug in elastic, but
                    // this is also needed for elastic update of the textarea.
                    // Without this it does not 'notice' that we cleared it.
                    setTimeout(function () {
                        jQuery(window).trigger('resize');
                    }, 0);

                    // prevent double click warning for this form
                    jQuery('#plone-interact-overlay input').removeClass('submitting');

                };

                $scope.removeTask = function (task) {
                    $scope.messages.remove(task);
                };

                $scope.isMine = function (task) {
                    return task.from == $scope.username;
                };

            }
        });

    }
]);


app.directive('animate', function(){
    return function(scope, elm, attrs) {
        setTimeout(function() {
            elm.addClass('noti-box-show');
        });
    };
});

app.directive('remove', function(){
    return function(scope, elm, attrs) {
        elm.bind('click', function(e){
            e.preventDefault();
            var $parent = elm.closest('.noti-box-show');
            $parent.removeClass('noti-box-show');
            setTimeout(function(){
                scope.$apply(function(){
                    scope.$eval(attrs.remove);
                });
            }, 200);
        });
    };
});

app.filter('newlines', function () {
    return function(text) {
        return text.replace(/\n/g, '<br/>');
    };
});
