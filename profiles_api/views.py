from rest_framework.views import APIView
from rest_framework.response import Response
from profiles_api import serializers
from rest_framework import status
# Create your views here.


class HelloUserApi(APIView):
    """The test API"""

    serializer_class = serializers.UserApiSerializer

    def get(self, request, format=None):
        """Returns a list of API views features"""
        an_apivew = [
            'Uses HTTP methods as functions (get, put, patch, post, delete)',
            'It is similar to traditional Django View',
            'Gives you the most control over your logic',
            'Is mapped manually to URL',
        ]

        return Response({'message':'Hello API', 'an_apiview': an_apivew})

    def post(self, request):
        """Create a hello message with your name"""
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'

            return Response({"message":message})
        else:
            print(serializer.errors)
            return Response(
                serializer.errors,
                status.HTTP_400_BAD_REQUEST,
                )

    def put(self, request, pk=None):
        """Return a put reponse"""
        return Response({"message": "PUT CALL"})

    def patch(self, request, pk=None):
        """Return a patch response"""
        return Response({"message":"PATCH CALL"})

    def delete(self, request):
        """Perform a delete operation"""
        return Response({"message":"DELETED"})