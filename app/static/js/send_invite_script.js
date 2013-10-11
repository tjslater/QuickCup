$(document).ready(function () {
    profile = JSON.parse(localStorage.getItem('profile'));
    recipient = JSON.parse(localStorage.getItem('recipient'));

    init(recipient);
});

function init(recipient) {
    latitude = recipient.latitude;
    longitude = recipient.longitude;
    getNearbyPlaces(latitude, longitude);
}

function getNearbyPlaces(lat, lng) {
    $.ajax({
        type: 'GET',
        data: {
            location: lat + "," + lng,
            radius: 1600,
            types: "cafe",
            sensor: false
        },
        url: 'http://proxy-rocketu.rhcloud.com/google-places/',
        success: function (data) {
            listPlaces(data);
        },
        error: function (err) {
            console.log(err)
        }
    })
}

function listPlaces(data) {
    places = "";
    but = {
        pre: '<li><button class="btn btn-default" ',
        post: "</button></li>"
    };

    for (i = 0; i < 3; i++) {
        if (data[i] !== undefined) {
            places += but.pre + "id=" + i + ">" + data[i].name + but.post;
        }
        $('#places').html(places);
        $('#times').css('display', 'inline');
    }
    selectPlace(data)
}
function selectPlace(data) {
    console.log(data);
    $('button').on('click', function () {
        id = $(this).attr('id');
        $('button').removeClass('btn-primary');
        $(this).toggleClass('btn-primary');
        localStorage.setItem("meetingLocation", JSON.stringify(data[id]));
    });
}

$('#selectfield').on('click', function () {
    minutes = $('#selectfield').val();
    date = new Date();
    date.setTime(date.getTime() + (minutes * 60 * 1000));
    localStorage.setItem("meetingTime", date)
});

$('#submit').on('click', function(){
    window.location.href = "/send-invite-confirmation"
})
