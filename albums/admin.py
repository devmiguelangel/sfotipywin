from django.contrib import admin
from albums.models import Album


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_cover', 'slug', 'artist', )
    search_fields = ['name', 'cover', ]
    readonly_fields = ('slug', )

admin.site.register(Album, AlbumAdmin)
