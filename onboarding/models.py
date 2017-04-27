from django.db import models
import mainSite
import os
from django.conf import settings
# Create your models here.

BASE_DIR = os.path.dirname(mainSite.__file__)

class ImageSnapshot(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    nom = models.CharField(max_length=30, default='')
    model_pic = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT, 'onboarding/'),
                                  blank=True, null=True)
    def __str__(self):
        return self.nom
