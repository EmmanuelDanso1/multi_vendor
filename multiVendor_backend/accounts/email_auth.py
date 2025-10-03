# accounts/email_auth.py
from django.contrib.auth.backends import ModelBackend
from .models import User

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        print("EmailBackend.authenticate CALLED with:", email)  # Debug line
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            print(" No user found with email:", email)
            return None

        if user.check_password(password):
            print("Password correct for:", email)
            return user
        else:
            print("Invalid password for:", email)
        return None
