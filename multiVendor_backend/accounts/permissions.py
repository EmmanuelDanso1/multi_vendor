from rest_framework import permissions


class IsVendor(permissions.BasePermission):
    """
    Custom permission to allow only vendors to access certain views.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_vendor)


class IsCustomer(permissions.BasePermission):
    """
    Custom permission to allow only customers to access certain views.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_customer)


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Allow users to edit only their own objects, otherwise read-only.
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  # GET, HEAD, OPTIONS
            return True
        return obj.user == request.user
