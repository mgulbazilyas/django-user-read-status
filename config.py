# config.py (or settings_local.py)
from django.conf import settings

# Import custom models here
USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')
