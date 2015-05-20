var app = angular.module('app', []);

app.config(['routeProvider', function($routeProvider) {
    $routeProvider
        .when('/', {
            templateUrl: 'static/blog/js/views/hello_world.html',
            controller: 'newController'
        })
}]);