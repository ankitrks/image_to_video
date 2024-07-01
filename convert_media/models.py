from django.db import models

class TokenStore(models.Model):
    token = models.TextField(unique=True)  # Unique token field
    created_at = models.DateTimeField(auto_now_add=True)  # Timestamp of token creation

    def __str__(self):
        return self.token

class Media(models.Model):
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    status = models.CharField(max_length=20, default='uploaded')
