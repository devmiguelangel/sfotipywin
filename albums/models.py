from django.db import models
from slugify import slugify, slugify_unicode, Slugify, UniqueSlugify
from sorl.thumbnail import get_thumbnail
from artists.models import Artist


class Album(models.Model):
    name = models.CharField(max_length=140)
    cover = models.ImageField(upload_to='albums')
    slug = models.SlugField(max_length=140, blank=True, default='')
    artist = models.ForeignKey(Artist)

    def __str__(self):
        return self.name

    def natural_key(self):
        data = {
            'name': self.name,
            'cover': self.cover.path
        }
        return data

    def image_cover(self):
        return """
        <img src="{image}" alt="{name}" />
        """.format(image=get_thumbnail(self.cover, '50x50', quality=100).url,
                   name=self.name)

    image_cover.allow_tags = True

    def save(self, *args, **kwargs):
        custom_slugify = UniqueSlugify(to_lower=True)
        self.slug = custom_slugify(str(self))
        super(Album, self).save(*args, **kwargs)
