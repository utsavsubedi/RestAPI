from django.db import models

# Create your models here.

class MovieInfo(models.Model):

    name = models.CharField(max_length=50)
    duration = models.FloatField()
    description = models.TextField(max_length=200)
    genre = models.TextField(max_length=50, default = 'action')
    image = models.ImageField(upload_to = 'media', default='media/images/none.jpg')

    def __str__(self):
        return self.name