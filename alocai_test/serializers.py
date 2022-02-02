from abc import ABC

from rest_framework import serializers


class PkRequestSerializer(serializers.Serializer):
    pk = serializers.IntegerField(required=False, write_only=True)

    class Meta:
        fields = '__all__'


class SuccessResponseSerializer(serializers.Serializer):
    success = serializers.IntegerField()
    message = serializers.CharField()

    class Meta:
        fields = '__all__'
