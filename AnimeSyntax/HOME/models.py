from django.db import models
from django.utils import timezone

class Anime(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='posters/', null=True, blank=True)
    anime_studio = models.CharField(max_length=150)
    genre = models.CharField(max_length=60)
    age_rating = models.CharField(max_length=10)
    MPAA_rating = models.CharField(max_length=10)
    is_ongoing = models.BooleanField(default=False)
    kodik_id = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    # Другие поля...

    def __str__(self):
        return self.title

