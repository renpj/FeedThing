from django.conf.urls import include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from ft.views import *

urlpatterns = [

    url(r'^admin/', include(admin.site.urls)),


    url(r'^$', index),
    url(r'^refresh/$', read_request_listener),
    url(r'^help/$', help),
    url(r'^feeds/$', feeds),
    url(r'^allfeeds/$', allfeeds),

    url(r'^addfeed/$', addfeed),
    url(r'^importopml/$', importopml),
    url(r'^feedgarden/$', feedgarden),

    url(r'^downloadfeeds/$', downloadfeeds),


    url(r'^accounts/login/$',loginpage),
    url(r'^accounts/logout/$',logoutpage),
    url(r'^read/(?P<fid>.*)/(?P<qty>.*)/',readfeed),


    url(r'^manage/$',managefeeds),
    url(r'^subscription/list/$',subscriptionlist),
    
    url(r'^subscription/(?P<sid>.*)/unsubscribe/$',unsubscribefeed),
    url(r'^subscription/(?P<sid>.*)/details/$',subscriptiondetails),
    url(r'^subscription/(?P<sid>.*)/promote/$',promote),
    url(r'^subscription/(?P<sid>.*)/addto/(?P<tid>.*)/$',addto),


    url(r'^feed/(?P<fid>.*)/revive/$',revivefeed),
    #(r'^feed/(?P<fid>.*)/kill/$',killfeed),
    url(r'^feed/(?P<fid>.*)/test/$',testfeed),
    
]
