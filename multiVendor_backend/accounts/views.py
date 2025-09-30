from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from .models import User
from .serializers import RegisterSerializer, LoginSerializer
from .permissions import IsVendor

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LoginView(generics.GenericAPIView):
    permission_classes = (AllowAny,)
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = serializer.validated_data["user"]

        refresh = RefreshToken.for_user(user)

        return Response({
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id,
                "email": user.email,
                "role": user.role,
            }
        }, status=status.HTTP_200_OK)


class VendorDashboardView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated, IsVendor]

    def get(self, request):
        return Response({
            "message": f"Welcome Vendor {request.user.email}!",
            "shop": request.user.vendor_profile.shop_name if hasattr(request.user, "vendor_profile") else None,
        })

