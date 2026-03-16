"""
Utility functions for the blood_request app.
"""
from .models import Notification


def create_notification(user, message, link=None, actor=None):
    """
    Create a portal notification for a user.
    
    Args:
        user: The User receiving the notification
        message: Notification text
        link: Optional URL to navigate to when clicked
        actor: Optional User who triggered the notification
    """
    return Notification.objects.create(
        user=user,
        message=message,
        link=link or '',
        actor=actor,
    )
