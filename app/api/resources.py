from tastypie import fields

from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from app.models import User, Industry, Location, Invite
from tastypie.authorization import Authorization

class InviteResource(ModelResource):
    class Meta:
        queryset = Invite.objects.all()
        resource_name = "invites"
        always_return_data = True
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = Authorization()


class IndustryResource(ModelResource):
    class Meta:
        queryset = Industry.objects.all()
        resource_name = 'industry'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = Authorization()
        always_return_data = True
        filtering = {
            "name": ALL
        }


class LocationResource(ModelResource):
    class Meta:
        queryset = Location.objects.all()
        resource_name = 'location'
        always_return_data = True
        filtering = {
            "name": ALL
        }



class UserResource(ModelResource):
    industry = fields.ForeignKey(IndustryResource, 'industry', full=True)
    location = fields.ForeignKey(LocationResource, 'location', full=True)
    # invites = fields.ForeignKey(InviteResource, 'invites', full=True)

    class Meta:
        always_return_data = True
        queryset = User.objects.all()
        resource_name = 'user'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = Authorization()
        filtering = {
        'linkedin': ALL,
        'first_name': ALL,
        'last_name': ALL,
        'location': ALL,
        'industry': ALL
    }