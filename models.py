from django.db import models
from .config import USER_MODEL

class ReadStatus(models.Model):
    user = models.OneToOneField(USER_MODEL, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username}: {self.is_read}"

    @classmethod
    def reset_all_users_read_status(cls):
        """Set is_read to False for all users."""
        cls.objects.update(is_read=False)

    @classmethod
    def reset_user_read_status(cls, user):
        """Set is_read to False for a specific user."""
        read_status, created = cls.objects.get_or_create(user=user)
        read_status.is_read = False
        read_status.save()