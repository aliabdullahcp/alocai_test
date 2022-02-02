from drf_spectacular.utils import extend_schema

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from alocai_test import Helpers
from alocai_test.models import MediaTypes
from games.CustomMessages import ResponseMessage
from games.serializers import GameSerializer


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
