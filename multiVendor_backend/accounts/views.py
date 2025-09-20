from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model
from .models import VendorProfile
from .serializers import (
    RegisterSerializer,
    UserSerializer,
    VendorProfileSerializer,
)
from .permissions import IsVendor, IsCustomer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = []  # anyone can register


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


# -------------------------------
# Vendor Views
# -------------------------------
class VendorProfileView(generics.RetrieveUpdateAPIView):
    queryset = VendorProfile.objects.all()
    serializer_class = VendorProfileSerializer
    permission_classes = [IsAuthenticated, IsVendor]

    def get_object(self):
        return self.request.user.vendor_profile


# -------------------------------
# Customer Views
# -------------------------------
class CustomerProfileView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, IsCustomer]

    def get_object(self):
        return self.request.user
