coords = JSON.parse(localStorage.getItem('coords'));
profile = JSON.parse(localStorage.getItem('profile'));


function initializeMaps() {
    var map;
    var mapOptions = {
        zoom: 10,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    };
    map = new google.maps.Map(document.getElementById('map'), mapOptions);
    var infowindow = new google.maps.InfoWindow();
    var marker;
    var bounds = new google.maps.LatLngBounds();

    for (var i = 0; i < list.length; i++) {
        var lat = parseFloat(list[i].fields.latitude);
        var lng = parseFloat(list[i].fields.longitude);
        var pos = new google.maps.LatLng(lat, lng);

        bounds.extend(pos);
        marker = new google.maps.Marker({
            position: pos,
            map: map
        });
        google.maps.event.addListener(marker, 'mousedown', (function (marker, i) {
            return function () {
                getIndustry(list[i]);
                getLocation(list[i]);
                saveUserAddress(marker, list[i]);
                generateInfoWindow(marker, list[i], infowindow, map);
                generateModal(list[i]);
            }
        })(marker, i));
    }
    map.fitBounds(bounds);
}


function generateModal(list) {
    $('.modal-header').html("<h3>" + list.fields.first_name + " " + list.fields.last_name + "</h3>");
    about = "<a href='" + list.fields.profile_url + "'><img src='" + list.fields.picture_url + "'/></a>";
    about += "<p style='margin-top: 5px;'><em>" + list.fields.headline + "</em></p><hr>";
    about += "<p><strong>" + list.fields.industry + "</strong></p>"
    about += "<p>" + Faker.Lorem.paragraph() + "</p>"
    $('.modal-body').html(about)
}

function generateInfoWindow(marker, list, infowindow, map) {
    var fullName = list.fields.first_name + " " + list.fields.last_name;
    var content = "<button type='button' data-toggle='modal' data-target='#myModal'>" + fullName + "</button>";
    content += "<p><em> " + list.fields.headline + "</em></p>";
    content += "<p>from: " + list.fields.location + "</p>";
    content += "<p>industry: " + list.fields.industry + "</p>";
    if (list.fields.availability == "1") {
        content += '<button><a href="/send-invite/' + list.fields.linkedin + '" >'
            + "send invite" + '</a></button>';
    }
    else {
        content += '<button disabled>not available</button>';
    }
    content += "<p style='float: right'><img src='" + list.fields.picture_url + "'/></p>";


    infowindow.setContent(content);
    infowindow.open(map, marker);

}

function getIndustry(list) {
    $.ajax({
        async: false,
        dataType: "jsonp",
        type: "GET",
        url: "http://bootcamp.rocketu.com/api/v1/industry",
        success: function (data) {
            list.fields.industry = data.objects[list.fields.industry - 1].name
        }
    });
}

function getLocation(list) {
    $.ajax({
        async: false,
        dataType: "json",
        type: "GET",
        url: "http://bootcamp.rocketu.com/api/v1/location",
        success: function (data) {
            list.fields.location = data.objects[list.fields.location - 1].name
        }
    });
}

function saveUserAddress(marker, list) {
    geocoder = new google.maps.Geocoder();
    geocoder.geocode({ latLng: marker.position }, function (results, status) {
            inviteInfo = {
                address: results[0].formatted_address,
                latLng: marker.position,
                name: list.fields.first_name,
                photo: "<img src='" + list.fields.picture_url + "' />"
            };
            localStorage.setItem('inviteInfo', JSON.stringify(inviteInfo))
        }
    );
}