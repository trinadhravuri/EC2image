from django.db import models

# Create your models here.


class MyImages(models.Model):
    image_name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = '')

    def __str__(self):
        return self.image_name