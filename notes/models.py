from django.db import models
from django.utils import timezone


# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=255, blank=False, null=False)
    body = models.TextField(help_text="Type a note, if you dare",
                            blank=False,
                            null=False)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def update(self):
        self.updated_at = timezone.now()
        self.save
