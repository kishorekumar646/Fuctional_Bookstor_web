from rest_framework import serializers
from accounts.models import User, UserDocument, UserWithName

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'is_active', 'is_staff', 'is_superuser', 'date_joined']

class UserDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserDocument
        fields = '__all__'

class UserWithNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserWithName
        fields = '__all__'