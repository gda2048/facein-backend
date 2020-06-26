from rest_framework import serializers
from rest_framework.serializers import Serializer

from profiles.models import User


class LoginSerializer(Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class ProfileSerializer(serializers.ModelSerializer):
    """User serializer for manipulations made by user."""

    class Meta:
        model = User
        fields = ('pk',
                  'username',
                  'first_name', 'last_name', 'info',
                  'is_superuser', 'is_security', 'is_admin', 'is_blacklisted',
                  'date_joined', 'last_login')
        read_only_fields = ('pk',
                            'is_superuser', 'is_security', 'is_admin', 'is_blacklisted',
                            'date_joined', 'last_login')


class StaffSerializer(serializers.ModelSerializer):
    """User serializer for manipulations made by user admin."""

    class Meta:
        model = User
        fields = ('pk',
                  'username',
                  'first_name', 'last_name', 'info',
                  'is_superuser', 'is_security', 'is_admin', 'is_blacklisted',
                  'date_joined', 'last_login')
        read_only_fields = ('pk',
                            'is_superuser',
                            'date_joined', 'last_login')
