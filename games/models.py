import uuid

from django.core.validators import MinValueValidator
from django.db import models

from alocai_test.models import CharFieldSizes, DecimalSizes


class GameManager(models.Manager):
    def get_best_value(self, max_size: int):
        # order games by price highest on top and then by space lower on top to get best value
        queryset = self.get_queryset().order_by('-price', 'space').all()
        size_used = 0
        games_selected = []
        for game in queryset:
            temp_sum = game.space + size_used
            # check if adding game exceeds the size
            if temp_sum > max_size:
                # skip the game that doesn't fit
                continue
            games_selected.append(game)
            size_used += temp_sum

        return games_selected, size_used


class Game(models.Model):
    objects = GameManager()

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    name = models.CharField(max_length=CharFieldSizes.XXX_LARGE, unique=True)
    price = models.FloatField(validators=[MinValueValidator(0, 'Price should be greater than 0'), ])
    space = models.PositiveBigIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

