from django.db import models
from django.contrib.auth.models import User
# from micro.models import UserProfile

class FixedWingPost(models.Model):
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

    wing_Span_in_mm = models.IntegerField()
    wing_Area_in_mm2 = models.IntegerField()
    average_Chord_in_mm = models.IntegerField()
    weight_in_grams = models.IntegerField()
    cruise_Speed_in_mtr_per_s = models.IntegerField()
    microcontroller = models.CharField(max_length=100, )
    inertial_Measurement_Unit =  models.CharField(max_length=100, )
    RC_Receiver = models.CharField(max_length=250, )
    RC_Transmitter = models.CharField(max_length=250, )
    servos = models.CharField(max_length=250, )
    electronic_Speed_Contorller = models.CharField(max_length=250, )
    brushless_Motor = models.CharField(max_length=250, )

    # user_name = models.ForeignKey(User, default=None, on_delete = models.CASCADE)
    def __str__(self):
        return self.title

class FixedWingImages(models.Model):
    post = models.ForeignKey(FixedWingPost , default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
    imageInfo = models.CharField(max_length=300, default=None)
    def __str__(self):
        return self.post.title


class FixedWingVideo(models.Model):
    post = models.ForeignKey(FixedWingPost , default=None, on_delete=models.CASCADE)
    videoFile= models.FileField(upload_to='videos', null=True,)
    videoInfo= models.CharField(max_length=500)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.title + ": " + str(self.id)




class FixedWingComment(models.Model):
    post = models.ForeignKey(FixedWingPost, default=None, on_delete = models.CASCADE, related_name ='fixedwing_comments')
    user = models.ForeignKey(User, default=None, on_delete = models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # commenter_email = models.EmailField(max_length = 254, default = None)
    def __str__(self):
        full_string = str(self.post.user_name) + ' commented : ' + self.content
        return  full_string
