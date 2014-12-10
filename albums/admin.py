from django.contrib import admin

from albums.models import Album


class AlbumAdmin(admin.ModelAdmin):
	list_display = ('name', 'image_cover', )
	search_fields = ['name', 'cover', ]

admin.site.register(Album, AlbumAdmin)
