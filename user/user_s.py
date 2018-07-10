from user.user_m import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('user_id', 'email', 'login_platform', 'picture', 'name')

