from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from .models import VendorProfile

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_vendor", "is_customer"]


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "username", "email", "password", "confirm_password", "is_vendor", "is_customer"]

    def validate_password(self, value):
        """Use Django’s built-in password validators"""
        validate_password(value)  # raises ValidationError if invalid
        return value

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError({"password": "Passwords do not match"})
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            is_vendor=validated_data.get("is_vendor", False),
            is_customer=validated_data.get("is_customer", True),
        )
        if user.is_vendor:
            VendorProfile.objects.create(user=user, store_name=f"{user.username}'s Store")
        return user


class VendorProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorProfile
        fields = ["store_name", "store_description", "phone", "address"]
