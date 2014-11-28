from django.db import models
from artists.models import Artist
from albums.models import Album

class Track(models.Model):
	name = models.CharField(max_length=140)
	order = models.PositiveIntegerField()
	track_file = models.FileField(upload_to='track')
	artist = models.ForeignKey(Artist)
	album = models.ForeignKey(Album)

	def __str__(self):
		return self.name

	# def natural_key(self):
	# 	return (self.name, ) + self.artist.natural_key()