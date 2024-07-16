from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.response import Response

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username','email','password')
        extra_kwargs = {
            'password':{'write_only':True}
        }
    def save(self):
        Account = User(
            username = self.validated_data['username'],
            email = self.validated_data['email'],
        )
        password = self.validated_data['password']
        Account.set_password(password)
        Account.save()
        return Account
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(max_length = 14)