from django.db import models

# Create your models here.
class Commercial(models.Model):
    kind = models.CharField(max_length=200)
    card_description = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images/',  blank=False)
    date = models.DateField()
    brief_info = models.TextField()
    def __str__(self):
        return self.kind


class LearnPoints(models.Model):
    post = models.ForeignKey(Commercial , default=None, on_delete=models.CASCADE)
    point = models.CharField(max_length=500, blank=False)


class CommercialImages(models.Model):
    post = models.ForeignKey(Commercial , default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')
    image_info = models.CharField(max_length=300, default=None)
    def __str__(self):
        return self.post.kind


class CommercialVideo(models.Model):
    post = models.ForeignKey(Commercial , default=None, on_delete=models.CASCADE)
    videofile= models.FileField(upload_to='videos/', null=True,)
    video_info= models.CharField(max_length=500)
    timestamp   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post.kind + ": " + str(self.id)