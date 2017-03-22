from django.db import models

# Create your models here.


class ExampleModel(models.Model):
    model_pic = models.ImageField(upload_to='media/')
    def __str__(self):
        return self.model_pic
