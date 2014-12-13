from django.conf.urls import patterns, url
from tracks.views import TrackTopListView

urlpatterns = patterns('',
	url(r'^tracks/top/$', TrackTopListView.as_view(), name='track-top')
)