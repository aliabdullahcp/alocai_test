from rest_framework import serializers

from games.models import Game


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        exclude = ['created_at', 'updated_at', ]

