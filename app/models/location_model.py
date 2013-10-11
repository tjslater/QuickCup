from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=64)

    class Meta:
        app_label = 'app'

    def __unicode__(self):
        return self.name