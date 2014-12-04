from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'feedthing.views.home', name='home'),
    # url(r'^feedthing/', include('feedthing.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),


    (r'^$', 'feedthing.ft.views.index'),
    (r'^refresh/$', 'feedthing.ft.views.reader'),
    (r'^help/$', 'feedthing.ft.views.help'),
    (r'^feeds/$', 'feedthing.ft.views.feeds'),
    (r'^allfeeds/$', 'feedthing.ft.views.allfeeds'),

    (r'^addfeed/$', 'feedthing.ft.views.addfeed'),
    (r'^importopml/$', 'feedthing.ft.views.importopml'),
    (r'^feedgarden/$', 'feedthing.ft.views.feedgarden'),
    (r'^accounts/login/$','feedthing.ft.views.loginpage'),
    (r'^accounts/logout/$','feedthing.ft.views.logoutpage'),
    (r'^read/(?P<fid>.*)/(?P<qty>.*)/','feedthing.ft.views.readfeed'),


    (r'^manage/$','feedthing.ft.views.managefeeds'),
    (r'^subscription/list/$','feedthing.ft.views.subscriptionlist'),
    
    (r'^subscription/(?P<sid>.*)/unsubscribe/$','feedthing.ft.views.unsubscribefeed'),
    (r'^subscription/(?P<sid>.*)/details/$','feedthing.ft.views.subscriptiondetails'),
    (r'^subscription/(?P<sid>.*)/promote/$','feedthing.ft.views.promote'),
    (r'^subscription/(?P<sid>.*)/addto/(?P<tid>.*)/$','feedthing.ft.views.addto'),


    (r'^feed/(?P<fid>.*)/revive/$','feedthing.ft.views.revivefeed'),
    (r'^feed/(?P<fid>.*)/kill/$','feedthing.ft.views.killfeed'),
    


)
