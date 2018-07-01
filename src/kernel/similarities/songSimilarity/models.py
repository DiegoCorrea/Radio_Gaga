# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from src.data.song.models import Song
# Create your models here.


class SongSimilarity(models.Model):
    # IDS
    songBase = models.ForeignKey(
        Song, unique=False,
        related_name='SongSimilarity_right',
        on_delete=models.CASCADE
    )
    songCompare = models.ForeignKey(
        Song, unique=False,
        related_name='SongSimilarity_left',
        on_delete=models.CASCADE
    )
    # Datas
    similarity = models.FloatField(default=0.0, unique=False)
    # Timers
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = (('songBase', 'songCompare'),)

    def as_json(self):
        return dict(
            songBase=self.songBase,
            songCompare=self.songCompare,
            similarity=self.similarity
        )
