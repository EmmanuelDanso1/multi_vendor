from django.urls import path
from .views import (
    RegisterView,
    UserDetailView,
    VendorProfileView,
    CustomerProfileView,
)

urlpatterns = [
    # Common
    path("register/", RegisterView.as_view(), name="register"),
    path("me/", UserDetailView.as_view(), name="user-detail"),

    # Vendor endpoints
    path("vendor/profile/", VendorProfileView.as_view(), name="vendor-profile"),

    # Customer endpoints
    path("customer/profile/", CustomerProfileView.as_view(), name="customer-profile"),
]
