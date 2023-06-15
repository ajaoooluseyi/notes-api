from django.db import models
from django.contrib.auth.models import User


class Note(models.Model):
    TEXT = 'text'
    AUDIO = 'audio'
    VIDEO = 'video'
    NOTE_TYPES = [
        (TEXT, 'Text'),
        (AUDIO, 'Audio'),
        (VIDEO, 'Video'),
    ]
    note_type = models.CharField(max_length=10, choices=NOTE_TYPES)
    content = models.FileField(upload_to='notes/%Y/%m/%d')
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notes')


    def __str__(self):
        return f'{self.note_type} Note ({self.content.name})'
