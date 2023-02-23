from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    username  = models.OneToOneField(User, on_delete= models.CASCADE)
    image = models.ImageField(default='profile.jpeg', upload_to = 'profile_pics')
    bio = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f'{self.username} profile'