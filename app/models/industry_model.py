from django.db import models


class Industry(models.Model):
    name = models.CharField(max_length=60)

    class Meta:
        app_label = 'app'

    def __unicode__(self):
        return self.name