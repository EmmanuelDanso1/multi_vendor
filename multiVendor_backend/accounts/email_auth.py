# accounts/email_auth.py
import logging
from django.contrib.auth.backends import ModelBackend
from .models import User

logger = logging.getLogger(__name__)

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        logger.info("EmailBackend.authenticate called with: %s", email)

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            logger.warning("No user found with email: %s", email)
            return None

        if user.check_password(password):
            logger.info("Password correct for: %s", email)
            return user
        else:
            logger.warning("Invalid password for: %s", email)
        return None
