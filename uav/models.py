from django.db import models
from django.contrib.auth.models import User

class UavPost(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/',  blank=True)
    date = models.DateField()
    type = [
    ('BLDC','Electric motor'),
    ('IC', 'Internal combustion engine'),
    ]
    Rotor_type = models.CharField(max_length=4, choices=type, default='BLDC')
    RF_frequecy = models.DecimalField(max_digits=5, decimal_places=2)
    _unit_ = [('MHz','Mega Hertz'),
    ('GHz','Giga Hertz')]
    unit = models.CharField(max_length=3, choices=_unit_, default='GHz')
    user_name = models.ForeignKey(User, default=None, on_delete = models.CASCADE)
    def __str__(self):
        return self.title

class UavImages(models.Model):
    post = models.ForeignKey(UavPost , default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
    image_info = models.CharField(max_length=300, default=None)
    def __str__(self):
        return self.post.title

class Comment(models.Model):
    post = models.ForeignKey(UavPost, default=None, on_delete = models.CASCADE, related_name ='comments')
    user = models.ForeignKey(User, default=None, on_delete = models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    commenter_email = models.EmailField(max_length = 254, default = None)
