from django.db import models

# Create your models here.

class Instrument(models.Model):
    thumbnail = models.ImageField(upload_to = 'uploads/')
    title = models.CharField(max_length=80)
    sound = models.FileField(upload_to='sounds/')

    def __str__(self):
        return self.title