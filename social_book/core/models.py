from django.db import models

# Create your models here.
class Profile(models.Model):
    user = None
    id_user = None
    bio = None
    profileimg = models.ImageField(upload_to='profile_images', default='blank-profile-picture.jpg')
    location = None

