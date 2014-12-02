from django.shortcuts import render, HttpResponse
from django.core import serializers

from tracks.models import Track

def track_view(req, id):
	try:
		track = Track.objects.get(pk=id)
	except Track.DoesNotExist:
		track = None

	# data = serializers.serialize('json', [track], indent=4, use_natural_foreign_keys=True, use_natural_primary_keys=True)
	return render(req, 'track.html', {'track': track})
	# return HttpResponse(data, content_type='application/json')