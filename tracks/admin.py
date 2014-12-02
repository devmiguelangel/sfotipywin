from django.contrib import admin
from tracks.models import Track

from actions import export_as_excel


class TrackAdmin(admin.ModelAdmin):
    list_display = (
        'artist', 'name', 'album', 'order', 'player', 'is_avicii', )
    list_filter = ('artist', 'album', )
    search_fields = [
        'name', 'album__name', 'artist__first_name', 'artist__last_name', ]
    list_editable = ('name', 'album', )
    actions = (export_as_excel, )
    raw_id_fields = ('album', )
    # filter_horizontal = ('favorite_songs', )

    def is_avicii(self, obj):
        return obj.artist.id == 1

    is_avicii.boolean = True

admin.site.register(Track, TrackAdmin)
