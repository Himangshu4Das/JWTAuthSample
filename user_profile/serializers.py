# user_profile/serializers.py
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserProfileSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)  # Specify password field as write-only

    class Meta:
        model = get_user_model()  # Get the user model dynamically
        fields = ('id', 'username', 'email', 'password', 'role')  # Include 'password' field

    def create(self, validated_data):
        # Extract and remove the 'password' field from validated data
        password = validated_data.pop('password')

        # Create the user with the remaining validated data
        user = self.Meta.model(**validated_data)

        # Set the user's password
        user.set_password(password)

        # Save the user to the database
        user.save()

        return user
