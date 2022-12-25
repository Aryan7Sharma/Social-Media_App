from django.db import models

# Create your models here.
class Profile(models.Model):
    user = None
    id_user = None
    bio = None
    profileimg = None
    location = None

