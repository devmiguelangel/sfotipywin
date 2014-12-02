from django.db import models
from artists.models import Artist
from albums.models import Album


class Track(models.Model):
    name = models.CharField(max_length=140)
    order = models.PositiveIntegerField()
    track_file = models.FileField(upload_to='tracks')
    artist = models.ForeignKey(Artist)
    album = models.ForeignKey(Album)

    # favorite_songs = models.ManyToManyField(
    #     Artist, blank=True, related_name='favorite_of')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/track/{id}/'.format(id=self.id)

    def player(self):
        return """
		<audio controls>
		  <source src="{track_file}" type="audio/mpeg">
		Your browser does not support the audio element.
		</audio>
    	""".format(track_file=self.track_file.url)

    player.allow_tags = True
    player.admin_order_field = 'track_file'

# def natural_key(self):
# 	return (self.name, ) + self.artist.natural_key()
