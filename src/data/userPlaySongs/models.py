# Create your models here.
from django.db import models

from src.data.user.models import User
from src.data.song.models import Song


class UserPlaySongs(models.Model):
    user = models.ForeignKey(
        User,
        unique=False,
        related_name='user',
        on_delete=models.CASCADE
    )
    song = models.ForeignKey(
        Song,
        unique=False,
        related_name='song',
        on_delete=models.CASCADE
    )
    play_count = models.IntegerField(default=0, unique=False)

    def as_json(self):
        return dict(
            user_id=self.user_id,
            song_id=self.song_id,
            play_count=self.play_count,
            )
