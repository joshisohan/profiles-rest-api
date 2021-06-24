from rest_framework import serializers


class UserApiSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=10)