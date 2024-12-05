#imports

from rest_framework import serializers
from resApp.models import Users

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users
        fields = ['id', 'username', 'email', 'fullname', 'isAdmin','createdAt']

        