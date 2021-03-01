from django.contrib import admin
from .models import Speaker, Speeches, Comment

class SpeakerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'middle_name')
    fields = ['first_name', 'middle_name', 'last_name', 'Bio']

admin.site.register(Speaker, SpeakerAdmin)

#admin.site.register(Speeches)
#admin.site.register(Speaker)

@admin.register(Speeches)
class SpeechesAdmin(admin.ModelAdmin):
    list_display = ('title', 'Speaker', 'date_of_post')
    
admin.site.register(Comment)