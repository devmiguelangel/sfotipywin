from django.db import models
from slugify import slugify, slugify_unicode, Slugify, UniqueSlugify


class Artist(models.Model):
    first_name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140, blank=True)
    biography = models.TextField(blank=True)
    slug = models.SlugField(max_length=140, blank=True, default='')
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

    def save(self, *args, **kwargs):
        custom_slugify = UniqueSlugify(to_lower=True)
        self.slug = custom_slugify(str(self))
        super(Artist, self).save(*args, **kwargs)

    # class Meta:
    #   unique_together = (('first_name', 'last_name'),)
