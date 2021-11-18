from django.db import models
from django.contrib.auth.models import AbstractUser

from apps.base.models import BaseModel
from apps.user.managers import UserManager


# Create your models here.
class User(BaseModel, AbstractUser):
    objects = UserManager()
    username = None
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["password"]
    email = models.EmailField(unique=True, db_index=True)


class UserProfile(BaseModel):
    user = models.OneToOneField(
        to=User, on_delete=models.CASCADE, related_name="profile"
    )
    # plan = models.ForeignKey(to=Plan, on_delete=models.CASCADE)
