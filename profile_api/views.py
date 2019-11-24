from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from profile_api import serializers
from profile_api import models


class HelloApiView(APIView):
    """ Test APIView """
    serializer_class = serializers.HelloSerializer

    def get(self, request, format=None):
        """ Return a list of APIView feature """
        an_apiview = [
            'Uses HTTP method as functions (get, post, put, patch, and delete)',
            'Is similar to a traditional Django view',
            'Gives you most control over your application logic',
            'Is mapped manually to URLs'
        ]
        return Response({'message': 'Hello', 'an_apiview': an_apiview})

    def post(self, request):
        """ Create a hello message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST

            )

    def put(self, request, pk=None):
        """ Handle updating an object """
        return Response({'method': 'PUT'})

    def patch(self, request, pk=None):
        """ Handle a partial update of an object """
        return Response({'method': 'PATCH'})

    def delete(self, request, pk=None):
        """ Delete an object """
        return Response({'method': 'DELETE'})


class HelloViewSet(viewsets.ViewSet):
    """ Test API ViewSet """

    serializer_class = serializers.HelloSerializer

    def list(self, request):
        """ Return a hello method """
        a_viewset = [
            'Uses action(list, create, retrieve, update, partial_update)',
            'Automatically maps to URLs using Routers',
            'Provide more functionality with less code'
        ]
        return Response({'message': 'Hello!!', 'a_viewset': a_viewset})

    def create(self, request):
        """ Create a hello message with our name """
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}!'
            return Response({'message': message})
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST

            )

    def retrieve(self, request, pk=None):
        print('Retrieve method call')
        return Response({'httm_method': 'GET'})

    def update(self, request, pk=None):
        print('update method call')
        return Response({'httm_method': 'PUT'})

    def partial_update(self, request, pk=None):
        print('partial update method call')
        return Response({'httm_method': 'PATCH'})

    def destroy(self, request, pk=None):
        print('destroy method call')
        return Response({'httm_method': 'DELETE'})


class UserProfileViewSet(viewsets.ModelViewSet):
    """ handle creating and updating profiles """
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
