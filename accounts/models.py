from django.contrib import auth
from django.db import models
from django.utils import timezone


class User(auth.models.User, auth.models.PermissionsMixin):
    #heavy lifting is being done by User & django(permissionsMixin)
    def __str__(self):
        return "@{}".format(self.username)
