# Create your models here.
from django.db import models

from apps.data.user.models import User
from apps.data.song.models import Song


class UserPlaySongs(models.Model):
    user = models.ForeignKey(User, unique=False, related_name='user')
    song = models.ForeignKey(Song, unique=False, related_name='song')
    play_count = models.IntegerField(default=0, unique=False)

    class Meta:
        unique_together = (('user', 'song'),)

    def as_json(self):
        return dict(
            user_id=self.user_id,
            song_id=self.song_id,
            play_count=self.play_count,
            )
