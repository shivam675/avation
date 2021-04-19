from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    image = models.ImageField(upload_to='images/',  blank=False)
    url = models.URLField(blank=False)

    def __str__(self):
        return self.title


class Division(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    division = models.ForeignKey(Division, default=None, on_delete = models.CASCADE, related_name ='tags')
    name = models.CharField(max_length=100)
    colour_list = [
    ('primary', 'ORANGE'),
    ('info', 'BLUE'),
    ('success', 'GREEN'),
    ('warning', 'YELLOW'),
    ('danger', 'RED'),
    ('neutral', 'GREY'),
    ]
    colour = models.CharField(max_length=12, choices=colour_list, default='warning')
    heading = models.CharField(max_length=200)
    body = models.CharField(max_length=300)
