from django.db import models
import mainSite
import os
from django.conf import settings
from django.core.validators import RegexValidator
# Create your models here.

BASE_DIR = os.path.dirname(mainSite.__file__)

class ImageSnapshot(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    nom = models.CharField(max_length=30, default='')
    model_pic = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT, 'onboarding/'),
                                  blank=True, null=True)
    def __str__(self):
        return self.nom


class UserContact(models.Model):
    name_regex = RegexValidator(
        regex=r'^[A-Za-z1-9ÑñÃãÁáÀàÂâÇçÉéÊêÍíÕõÓóÔôÚúÜü]+((\-| )[A-Za-z1-9ÑñÃãÁáÀàÂâÇçÉéÊêÍíÕõÓóÔôÚúÜü]+)*$',
        message='Must be an alphanumeric',
    )
    nationality_regex = RegexValidator(
        regex=r'^[A-Za-z]*$',
        message='Must be a 2-4 capital letter word',
    )
    date_regex = RegexValidator(
        regex=r'^\d{4}-\d{2}-\d{2}$',
        message='Must be a Date',
    )
    dni_regex = RegexValidator(
        regex=r'^[0-9]{8}[A-Z]{1}$',
        message='Must be 8 numbers followed by 1 capital letter',
    )
    sex_regex = RegexValidator(
        regex=r'^[A-Z]{1}$',
        message='Must be 8 numbers followed by 1 capital letter',
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField('First Name', max_length=40, validators=[name_regex])
    last_name = models.CharField('Last Name', max_length=40, blank=True, validators=[name_regex])
    nationality = models.CharField('Nationality', max_length=10, validators=[nationality_regex])
    dob = models.DateField('Birthdate', null=True, blank=True, validators=[date_regex])
    doe = models.DateField('Expiracydate', null=True, blank=True, validators=[date_regex])
    sex = models.CharField('sex', max_length=1, blank=True, validators=[sex_regex])
    dni = models.CharField('DNI', max_length=9, validators=[dni_regex])

    front_pic = models.ImageField(upload_to=os.path.join('', 'onboarding/userpictures/'),
                                  blank=True, null=True)
    back_pic = models.ImageField(upload_to=os.path.join('', 'onboarding/userpictures/'),
                                  blank=True, null=True)

