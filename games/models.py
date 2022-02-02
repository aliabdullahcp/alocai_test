from django.core.validators import MinValueValidator
from django.db import models

from alocai_test.models import CharFieldSizes, DecimalSizes


class Game(models.Model):
    id = models.UUIDField(primary_key=True)

    name = models.CharField(max_length=CharFieldSizes.XXX_LARGE, unique=True)
    price = models.DecimalField(decimal_places=DecimalSizes.Price.DECIMAL_PLACES,
                                max_digits=DecimalSizes.Price.MAX_DIGITS,
                                validators=[MinValueValidator(0.0, 'Price should be greater than 0'), ])
    space = models.PositiveBigIntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

