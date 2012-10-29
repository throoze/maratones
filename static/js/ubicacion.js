var map;
var marker;
lasimon = new google.maps.LatLng(10.409089, -66.883013);

function initialize() {
    var myOptions = {
        zoom: 17,
        center: lasimon,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById("map-canvas"),
        myOptions);
    marker = new google.maps.Marker({
        position: lasimon, 
        map: map, 
        title:"Maratones Super Regionales de la ACM-ICPC"
    });
}

$(document).ready(function(){
    initialize();
});