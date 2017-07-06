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

class ImageSnapshot(models.Model):
    name_regex = models.RegexValidator(
        regex=r'^[A-Za-z1-9ÑñÃãÁáÀàÂâÇçÉéÊêÍíÕõÓóÔôÚúÜü]+((\-| )[A-Za-z1-9ÑñÃãÁáÀàÂâÇçÉéÊêÍíÕõÓóÔôÚúÜü]+)*$',
        message=_('Must be an alphanumeric'),
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)
    firstname = models.UpperCaseCharField(_('First Name'), max_length=40, validators=[name_regex])
    lastname = models.UpperCaseCharField(_('Last Name'), max_length=40, blank=True, validators=[name_regex])
    model_pic = models.ImageField(upload_to=os.path.join(settings.MEDIA_ROOT, 'onboarding/'),
                                  blank=True, null=True)

    def __str__(self):
        return self.nom

#class AbstractPersonInfo(ClientDataCIMDBaseModel):
    """Generic class to store personal information. To
    be used for Traders, Middle/Back office people, etc. """
'''
    def check_filename(self, filename):
        filename = os.path.basename(filename)
        if not filename:
            return None
        return "/".join(('contactphotos', filename))

    # See http://stackoverflow.com/questions/19130942/whats-the-best-way-to-store-phone-number-in-django-models
    name_regex = RegexValidator(
        regex=r'^[A-Za-z1-9ÑñÃãÁáÀàÂâÇçÉéÊêÍíÕõÓóÔôÚúÜü]+((\-| )[A-Za-z1-9ÑñÃãÁáÀàÂâÇçÉéÊêÍíÕõÓóÔôÚúÜü]+)*$',
        message=_('Must be an alphanumeric'),
    )

    active = models.BooleanField(_('Active'), default=True)
    CONTACT_TYPE_PERSON = 'P'
    CONTACT_TYPE_GROUP = 'G'

    TYPE_CHOICES = (
        (CONTACT_TYPE_PERSON, _('Person')),
        (CONTACT_TYPE_GROUP, _('Group')),
    )
    type = models.CharField(_('Type'),
                            max_length=1,
                            choices=TYPE_CHOICES,
                            default=CONTACT_TYPE_PERSON,
                            db_index=True,
                            help_text=_('Use \'Person\' contact for a physical person (real person).\
                            You will need to fill up Name, Last Name and Citizenship.<br>Use \'Group\' contact\
                            when it is used to group several emails for notifications (Back Office STP for example)'))
    name = UpperCaseCharField(_('Name'), max_length=30, validators=[name_regex])
    lastname = UpperCaseCharField(_('Last Name'), max_length=40, blank=True, validators=[name_regex])
    lastname2 = UpperCaseCharField(_('Last Name 2'), max_length=40, blank=True, validators=[name_regex])
    displayname = UpperCaseCharField(_('Display Name'), max_length=110, blank=True,
                                     validators=[name_regex], help_text=_('Contact display to be used in Office365 (Email) and Intranet (Optional field)<br>\
                                   If empty and citizenship set to Portugal, the contact display is automatically generated using \'Name\' + \'Last Name 2\'<br>\
                                   if empty and citizenship is not set to Portugal, the contact display is automatically generated using \'Name\' + \'Last Name\''))
    terminated = models.DateField('Terminated', null=True, blank=True)
    groups = models.ManyToManyField(Group, blank=True)
    picture = models.ImageField(_('Picture'), upload_to=check_filename, blank=True, max_length=64)
    citizenship = models.ForeignKey(Country, null=True, blank=True,
                                    help_text=_('Only mandatory for person contact (not group contact)'))
'''

#class Contact(AbstractPersonInfo):
"""Class to store information of a contact"""
'''
    # Static data
    _stp_notification_url = None

    # Fields
    department = models.ForeignKey(Department,
                                   limit_choices_to=dict(active__exact=True,
                                                         legalentity__active__exact=True
                                                         ),
                                   related_name='departmentcontacts')
    manager = models.ForeignKey('self', null=True, blank=True, related_name='employeecontacts')

    aliases = GenericRelation(
        Alias,
        content_type_field='object_type',
        object_id_field='object_id',
        null=True,
        related_query_name='alias_contact',
    )
    trading = models.BooleanField(
        default=False, null=False, blank=False,
        help_text=_("Indicates if the person is a Trader or Broker. This information "
                    "is critical to filter Traders in trade capture screens, and for "
                    "Compliance purpose (Mifid II)"),
    )
    identification = models.CharField(
        max_length=20, null=True, blank=True,
        help_text=_("DNI/NIE/PASSPORT. Mandatory field for Trader or Broker (Mifid)."),
    )
    birthdate = models.DateField(
        null=True, blank=True,
        help_text=_("Mandatory field for Trader or Broker (Mifid).")
    )
'''