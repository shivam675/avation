from django.db import models

# Create your models here.
class Training(models.Model):
    kind = models.CharField(max_length=200)
    card_description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/',  blank=False)
    date = models.DateField()
    def __str__(self):
        return self.kind

class TrainingImages(models.Model):
    post = models.ForeignKey(Training , default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
    image_info = models.CharField(max_length=300, default=None)
    def __str__(self):
        return self.post.kind


class TrainingVideo(models.Model):
    post = models.ForeignKey(Training , default=None, on_delete=models.CASCADE)
    videofile= models.FileField(upload_to='videos/', null=True,)
    video_info= models.CharField(max_length=500)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.kind + ": " + str(self.id)