from rest_framework import serializers

from profile_api import models


class HelloSerializer(serializers.Serializer):
    """ Serializers a name field for testing APIVew """

    name = serializers.CharField(max_length=20)


class UserProfileSerializer(serializers.ModelSerializer):
    """ A serializer that handle user profile objects """

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """ Create and return a new User """
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user
