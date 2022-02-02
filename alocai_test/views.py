from drf_spectacular.utils import extend_schema

from django.db import connection

from rest_framework.decorators import api_view, parser_classes

from alocai_test import Helpers
from alocai_test.models import MediaTypes
from alocai_test.serializers import SuccessResponseSerializer
from .CustomMessages import ResponseMessage


@extend_schema(
    responses={
        (200, MediaTypes.JSON): SuccessResponseSerializer,
    },
)
@api_view(['GET', 'HEAD'])
def health_check(request):
    response_dict = {
        'database': "healthy"
    }

    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            return Helpers.SuccessResponse(response_dict)
    except Exception as ex:
        response_dict['database'] = "unhealthy"
        return Helpers.ErrorResponse(ResponseMessage.something_went_wrong, response_dict)
