from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sfotipywin.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^track/(?P<id>[0-9]{1})/$', 'tracks.views.track_view', name='track'),
    url(r'^signup/$', 'userprofiles.views.signup', name='signup'),
    url(r'^signin/$', 'userprofiles.views.signin', name='signin'),
)

# if settings.DEBUG: # Manejar archivos estaticos en Mono DEBUG
urlpatterns += patterns('',
	url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))