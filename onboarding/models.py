from django.db import models

# Create your models here.


class ImageSnapshot(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    model_pic = models.ImageField(max_length=500, upload_to='onboarding/')
