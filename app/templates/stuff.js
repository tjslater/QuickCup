var Beer = Backbone.Model.extend({
    urlRoot: 'api/v1/nearby',
    url: function(){
        beer_url = Backbone.Model.prototype.url.apply(this);
        if (lat1 && lon1){
            beer_url + '?lat=' + lat1 + '&lng=' + lon1;
        }
        return beer_url;
    }
});

if (navigator.geolocation){
    navigator.geolocation.getCurrentPosition(function(position){
        lat1 = position.coords.latitude;
        lon1 = position.coords.longitude;
        var router = new Workspace; //router instance
        Backbone.history.start();
    });
}

/////////////
