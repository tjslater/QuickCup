from django.db import models



class Invite(models.Model):
    invite_to = models.ForeignKey("User", related_name="recipient")
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        app_label = 'app'

    def __unicode__(self):
        return "invite to", self.invite_to