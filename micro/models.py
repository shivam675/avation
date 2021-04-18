from django.db import models
from django.contrib.auth.models import User



class UserProfile(models.Model):
    deg = [('user', 'user'),
        ('customer', 'customer'),
        ('staff', 'staff')
    ]
    name = models.CharField(max_length=250, default=User)
    designation = models.CharField(max_length=10, choices=deg, default = 'user')
    email = models.EmailField(max_length=250, blank=False)
    profile_photo = models.ImageField(upload_to='profiles/', default='default_img/default-avatar.png')
    bio = models.TextField(max_length=1000)
    background = models.ImageField(upload_to='user_backgrounds/', default='default_img/bg8.jpg')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.name
