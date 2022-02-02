from drf_spectacular.utils import extend_schema

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from alocai_test import Helpers
from alocai_test.models import MediaTypes
from games.CustomMessages import ResponseMessage
from games.models import Game
from games.serializers import GameSerializer, BestValueResponseSerializer, BestValueRequestSerializer


@extend_schema(
    responses={
        (200, MediaTypes.JSON): GameSerializer,
    },
    request={
        MediaTypes.JSON: GameSerializer
    },
)
@api_view(['POST'])
@parser_classes([JSONParser])
def create(request):
    serializer = GameSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Helpers.SuccessResponse(serializer.data)
    else:
        return Helpers.ErrorResponse(ResponseMessage.serializer_error, body=serializer.errors)


@extend_schema(
    responses={
        (200, MediaTypes.JSON): BestValueResponseSerializer,
    },
    parameters=[
        BestValueRequestSerializer
    ],
)
@api_view(['POST'])
def get_best_value(request):
    serializer = BestValueRequestSerializer(data=request.GET)
    if serializer.is_valid():
        pen_drive_space = serializer.validated_data.get('pen_drive_space')
        best_value_games, space_used = Game.objects.get_best_value(pen_drive_space)
        response_serializer = BestValueResponseSerializer({
            "games": best_value_games,
            "total_space": space_used,
            "remaining_space": pen_drive_space - space_used
        })
        return Helpers.SuccessResponse(response_serializer.data)
    else:
        return Helpers.ErrorResponse(ResponseMessage.serializer_error, body=serializer.errors)
