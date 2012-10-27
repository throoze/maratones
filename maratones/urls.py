from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'maratones.views.home', name='home'),
    # url(r'^maratones/', include('maratones.foo.urls')),
    url(r'^$', 'maratones.views.home'),
    url(r'^ubicacion$', 'maratones.views.ubicacion'),
    url(r'^itinerario$', 'maratones.views.itinerario'),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
