from django.contrib import admin

from .models import Film

# Register your models here.

class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'director')

    fieldsets = (
        (None, {
        'fields': ('title', 'slug', 'description', 'director', 'image', 'trailer_embed')
        }),
        ('True/False Conversation', {
            'classes': ('collapse',),
            'fields': ('convo_author', 'convo_text', 'convo_audio')
        }
        )
    )

admin.site.register(Film, FilmAdmin)