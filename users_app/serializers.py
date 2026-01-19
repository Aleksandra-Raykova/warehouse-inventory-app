from users_app.models import CustomUser
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        max_length=150,
        min_length=5,
        write_only=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = CustomUser
        fields = ['email', 'first_name', 'last_name', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True, 'max_length': 150, 'min_length': 5}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError("Passwords must be the same")
        return attrs

    def create(self, validated_data):
        validated_data.pop('password2')
        password = validated_data.pop('password')

        user = CustomUser.objects.create_user(**validated_data)
        user.set_password(password)
        user.save()

        return user
