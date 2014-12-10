from django.contrib import admin
from userprofiles.models import UserProfile, UserTrack


class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'avatar', )


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserTrack)
