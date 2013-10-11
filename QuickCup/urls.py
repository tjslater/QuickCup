from django.conf.urls import patterns, include, url
from django.contrib import admin
from tastypie.api import Api
from app.api.resources import UserResource, IndustryResource, LocationResource

v1_api = Api(api_name='v1')
v1_api.register(UserResource())
v1_api.register(IndustryResource())
v1_api.register(LocationResource())
####
admin.autodiscover()

urlpatterns = patterns('app.views',
                       url(r'^feed$', 'feed_view.feed', name='feed'),
                       url(r'^$', 'login_view.login', name='login'),
                       url(r'^user-search$', 'user_search_view.user_search', name='user-search'),
                       url(r'^map-locations$', 'map_locations_view.map_locations', name='map_locations'),
                       url(r'^meeting-confirmed$', 'meeting_confirmed_view.meeting_confirmed',
                           name='meeting_confirmed'),

                       url(r'^profile$', 'profile_view.profile', name='profile'),
                       url(r'^send-invite/(?P<recipient>[-\w]+)', 'send_invite_view.send_invite', name="send_invite"),
                       url(r'^send-invite-confirmation$', 'send_invite_confirm_view.send_invite_confirm',
                           name="send_invite_confirm"),
                       url(r'^api/', include(v1_api.urls)),
                       url(r'^test', 'test_view.test', name='test'),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
)