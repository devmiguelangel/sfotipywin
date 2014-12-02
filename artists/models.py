from django.db import models


class Artist(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140, blank=True)
    biography = models.TextField(blank=True)
    favorite_songs = models.ManyToManyField(
        'tracks.Track', blank=True, related_name='favorite_of')

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def natural_key(self):
        # return (self.first_name, self.last_name, self.biography)
        data = {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'biography': self.biography
        }
        return data

    # class Meta:
    # 	unique_together = (('first_name', 'last_name'),)
