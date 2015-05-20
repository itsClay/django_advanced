app.controller('newController', function($http){
    // Controller logic goes here
    console.log('Our controller is working')
    $hhtp.get('http://localhost:8000/api/blog/entries')
        .then(function(data) {
            console.log(data)
        })
});