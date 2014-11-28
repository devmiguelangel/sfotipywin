from django.db import models
from artists.models import Artist

class Album(models.Model):
	name = models.CharField(max_length=140)
	cover = models.ImageField(upload_to='album')
	artist = models.ForeignKey(Artist)

	def __str__(self):
		return self.name

	def natural_key(self):
		data = {
			'name': self.name,
			'cover': self.cover.path
		}
		return data