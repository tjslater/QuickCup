QuickCup is a professional personalized networking application. The idea behind it is that while meetups and other networking events serve well as general approaches to making connections, QuickCup is a tool for direct one-on-one contact.

You login, find other people using quickcup nearby who are also in your industry, and you send them an invite to a cup of coffee in the form of a text message from the application which sends their profile, contact information, and a message.
They have 30 minutes to reply, after which the invitation expires. 

APIs
- LinkedIn login and Oauth
- GoogleMaps
  - GoogleMaps locations
  - GoogleMaps directions
  - GoogleMaps Markers
- Twilio SMS

Backend:
- Django
  - forms and validation
  - security
  - templating and routing
  - MySQL integration
  - API routing and endpoints for frontend integration

Database:
- MySQL

Frontend:
- HTML
- CSS
  - Bootstrap
- Javascript
  - jQuery
    - Vegas, jQuery slideshow plugin

-----------------
Next iteration

Backbone connected to relational database API
- Backbone
  - Backbone-tastypie for API compatibility
  - Backbone-Relational for DB compatibility
  - Backbone-Filtered Collection for filtering by geolocation coordinates
  - Backbone-local storage for backbone compatible local storage

- RequireJS to handle loading 3rd party libraries

- Underscore, Backbone depedency
