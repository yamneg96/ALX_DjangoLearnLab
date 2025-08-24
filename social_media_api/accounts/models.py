# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

def user_upload_path(instance, filename):
    return f"profile_pics/{instance.username}/{filename}"

class User(AbstractUser):
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to=user_upload_path, blank=True, null=True)
    # One M2M to self with asymmetric follows:
    # "followers" gives you reverse "following" automatically
    followers = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="following",
        blank=True
    )

    def __str__(self):
        return self.username
