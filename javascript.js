console.info('spa_directions.js loaded');

/* code for simple map */
const directionsInfo = document.querySelector('#directions-info');
const directionsButton = document.querySelector('#get-directions');
const travelTime = document.querySelector('#travel-time');
directionsButton.addEventListener('click', getLocation);
let directionsService;
let directionsDisplay;

function getLocation() {

    navigator.geolocation.getCurrentPosition(function(position) {
        directionsInfo.innerHTML = `Your coordinates: (${position.coords.latitude}, ${position.coords.longitude})`;
        var pos = new google.maps.LatLng(position.coords.latitude, position.coords.longitude);
        initMap(pos);
    });
}

function initMap(location) {

    // Instantiate a directions service.
    directionsDisplay = new google.maps.DirectionsRenderer(rendererOptions);
    directionsMap = new google.maps.Map(document.querySelector('#directions-map'), {
        center: location,
        zoom: 16
    });
    //GR added this 2022-06 to suppress A & B markers.
    var rendererOptions = {
        map: directionsMap,
        draggable: true,
        suppressMarkers: true
    }
    directionsDisplay = new google.maps.DirectionsRenderer(rendererOptions);
    //end of stuff added

    directionsService = new google.maps.DirectionsService();

    directionsDisplay.setMap(directionsMap);
    let destination = new google.maps.LatLng(47.6795273, -70.8697928);
    //18.211685, -67.141684
    destination = new google.maps.LatLng(18.211685, -67.141684);
    destination = "Fuertes Observatory, Ithaca, NY 14850";

    calcRoute(location, destination);

}

function calcRoute(start, destination) {
    let request = {
        origin: start,
        destination: destination,
        travelMode: google.maps.TravelMode.DRIVING //
    };

    directionsService.route(request, function(response, status) {
        if (status == 'OK') {
            directionsDisplay.setDirections(response);
            var point = response.routes[0].legs[0];
            //$( '#travel_data' ).html( 'Estimated travel time: ' + point.duration.text + ' (' + point.distance.text + ')' );
            //travelTime.innerHTML = "\t Estimated Travel Time: " + point.duration.text + "\t Distance: " + point.distance.text;
            //directionsInfo.innerHTML += "\t Estimated Travel Time: " + point.duration.text + "\t Distance: " + point.distance.text;
            travelTime.innerHTML = `Estimated Travel Time: ${point.duration.text}, Distance: ${point.distance.text}`;
            let starter = new google.maps.Marker({
                position: start,
                map: directionsMap,
                label: {
                    text: 'You',
                    color: "#f3f3f3",
                    fontSize: "16px",
                    fontWeight: "bold"
                }
            });
            let marker = new google.maps.Marker({
                position: destination,
                map: directionsMap,
                label: 'Ambulance'
            });
        }

    })
}