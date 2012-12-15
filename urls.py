from django.conf.urls import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin, auth
from django.http import HttpResponse

admin.autodiscover()

urlpatterns = patterns('',
    #robots
    (r'^robots\.txt$', lambda r: HttpResponse("User-agent: *\nDisallow: /", mimetype="text/plain")),


    #admin
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?i)about', 'Home.views.About', {}, 'about'),
    url(r'^(?i)contact', 'Home.views.Contact', {}, 'contact'),
    url(r'^(?i)christmas', 'Home.views.Christmas'),
    url(r'^(?i)SendEmail', 'Home.views.SendEmail'),
    url(r'^', 'Home.views.Index', {}, 'home')

)
