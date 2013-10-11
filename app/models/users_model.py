from django.db import models
from invite_model import Invite
from location_model import Location
from industry_model import Industry


class User(models.Model):
    # LINKEDIN DATA
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    join_date = models.DateTimeField(auto_now_add=True)
    linkedin = models.CharField(max_length=64)
    headline = models.CharField(max_length=128)
    picture_url = models.CharField(max_length=128)
    join_date = models.DateTimeField(auto_now_add=True)
    profile_url = models.CharField(max_length=128)
    # FOREIGN KEYS
    industry = models.ForeignKey(Industry, related_name="industry")
    location = models.ForeignKey(Location, related_name="location")
    # invites = models.ForeignKey(Invite, related_name="invites")
    # random geolocation coords
    latitude = models.CharField(max_length=64, default=0)
    longitude = models.CharField(max_length=64, default=0)

    # USER INPUT
    age = models.PositiveSmallIntegerField(max_length=3, default=0)
    experience = models.PositiveSmallIntegerField(max_length=2, default=0)
    availability = models.CharField(max_length=64, default=1)


    class Meta:
        app_label = 'app'

    def __unicode__(self):
         return self.linkedin