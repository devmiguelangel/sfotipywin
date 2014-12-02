from random import choice
from tracks.models import Track

nombres = ['miguel', 'juan', 'pedro', 'rolando', ]


def basico(req):
    tracks = Track.objects.all()

    selected_track = None
    for t in tracks:
        if t.get_absolute_url() == req.path:
            selected_track = t

    return {'title': choice(nombres), 'tracks': tracks, 'selected_track': selected_track}
