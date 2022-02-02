from django.core.validators import MinValueValidator
from rest_framework import serializers

from games.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        exclude = ['created_at', 'updated_at', ]


class BestValueRequestSerializer(serializers.Serializer):
    pen_drive_space = serializers.IntegerField(validators=[MinValueValidator(0)])


class BestValueResponseSerializer(serializers.Serializer):
    games = GameSerializer(many=True)
    total_space = serializers.IntegerField()
    remaining_space = serializers.IntegerField()

