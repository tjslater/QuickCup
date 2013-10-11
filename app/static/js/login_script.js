getLocation();

function getLocation() {
    if (navigator.geolocation) {
        console.log("getting location");
        navigator.geolocation.getCurrentPosition(showPosition);
    }
    else {
        alert("no geolocation found")
    }
}

function showPosition(position) {
    coords = {};
    coords.lat = position.coords.latitude;
    coords.lng = position.coords.longitude;
    localStorage.setItem('coords', JSON.stringify(coords))
}

function onLinkedInLoad() {
    IN.Event.on(IN, "auth", onLinkedInAuth);
}

function onLinkedInAuth() {
    /*IN.API.Profile("me")
        .fields("firstName", "lastName", "industry", "id", "headline", "pictureUrl", "location, profileUrl")
        .result(displayProfiles);*/
    IN.API.Connections("me")
        .fields("firstName", "lastName", "industry", "id", "headline", "pictureUrl", "location", "publicProfileUrl")
        .result(displayProfiles);
}

function displayProfiles(profiles) {
    var member = profiles.values[94];
    localStorage.setItem('profile', JSON.stringify(member));
    $(document).ready(function () {
        showWelcome(member)
    });
}

function showWelcome(member) {
        $('#id_first_name').val(member.firstName);
        $('#id_last_name').val(member.lastName);
        $('#id_headline').val(member.headline);
        $('#id_industry').val(member.industry);
        $('#id_linkedin').val(member.id);
        $('#id_picture_url').val(member.pictureUrl);
        $('#id_profile_url').val(member.publicProfileUrl);
        $('#id_location').val(member.location.name);
        $('#id_latitude').val(1);
        $('#id_longitude').val(1);
    message = "<h3>Thank you!</h3>";
    message += "<h4>You appear to be " + member.firstName + " " + member.lastName + ".</h4>";
    message += "<p>You also work in the " + member.industry + " industry.</p>";
    message += "<p><em>If this is correct, full steam ahead!</em></p>";
    message += "<button type='submit' class='btn btn-default' value='submit'>Submit</button>";
    $('form').append(message);
    $('#linkedin').fadeOut('fast');
    $('#greeting').fadeIn('slow')

}