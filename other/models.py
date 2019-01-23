"""Extra models for notifications."""
from uuid import uuid4
from django.db import models
from django.contrib.sessions.models import Session

class Device(models.Model):
    """A device to which a user is logged in.
    To be used chiefly for sending notifications."""

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    time_of_creation = models.DateTimeField(auto_now_add=True)
    last_ping = models.DateTimeField()

    user = models.ForeignKey('users.UserProfile', on_delete=models.CASCADE, related_name='devices')
    session = models.ForeignKey(Session, on_delete=models.CASCADE, related_name='devices')

    fcm_id = models.CharField(max_length=200, null=True, blank=True)

    application = models.CharField(max_length=50, blank=True)
    app_version = models.CharField(max_length=50, blank=True)
    platform = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.name

    def supports_rich(self):
        """Check if this device supports data messages."""

        # Check for flutter and iOS
        if self.application == 'app.insti.flutter':
            return False
        if self.application == 'app.insti.ios':
            return True

        # Try parsing the app version
        try:
            return int(self.app_version) >= 17
        except ValueError:
            return False