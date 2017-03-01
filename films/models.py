from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Film (models.Model):
    slug = models.SlugField(unique=True)
    title = models.CharField(max_length=1024)
    description = models.TextField()
    director = models.CharField(max_length=1024)
    image = models.ImageField(upload_to="images/film_images")
    trailer_embed = models.URLField(max_length=1024, null=True, blank=True)
    convo_author = models.CharField(max_length=1024, null=True, blank=True)
    convo_audio = models.URLField(max_length=1024, null=True, blank=True)
    convo_text = models.TextField(null=True, blank=True)

    def get_absolute_url(self):
        return "/films/%s/" % self.slug