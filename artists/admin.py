from django.contrib import admin

from artists.models import Artist
from tracks.models import Track
from albums.models import Album


class TrackInline(admin.StackedInline):
    model = Track
    extra = 1


class AlbumInline(admin.StackedInline):
    model = Album
    extra = 1


class ArtistAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', ]
    inlines = [
        TrackInline,
        AlbumInline,
    ]
    # filter_horizontal = ('favorite_songs', )
    filter_vertical = ('favorite_songs', )

admin.site.register(Artist, ArtistAdmin)
