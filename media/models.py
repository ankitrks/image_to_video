from django.db import models

# class Image(models.Model):
#     image = models.ImageField(upload_to='images/')
#     status = models.CharField(max_length=20, default='uploaded')

# class Video(models.Model):
#     video = models.FileField(upload_to='videos/')
#     image = models.OneToOneField(Image, on_delete=models.CASCADE)

class Media(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    status = models.CharField(max_length=20, default='uploaded')
