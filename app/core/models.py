from django.db import models
from django.utils.translation import ugettext_lazy as _

class Donor(models.Model):
    """ Donor model
    """
    SEX = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ]
    BG = [
        ('APOS','A+'),
        ('BPOS','B+'),
        ('OPOS','O+'),
        ('ANEG','A-'),
        ('BNEG','B-'),
        ('ONEG','O-'),
        ('ABPOS','AB+'),
        ('ABNEG','AB-'),
    ]
    firstname = models.CharField(_('First Name'), max_length=255, null=True, blank=True)
    lastname = models.CharField(_('Last Name'), max_length=255, null=True, blank=True)
    age = models.CharField(_('Age'), max_length=3, null=True, blank=True)
    sex = models.CharField(_('Sex'), max_length=6, null=True, blank=True,choices=SEX )
    location = models.CharField(_('Location'), max_length=20, null=True, blank=True)
    blood_group= models.CharField(_('Blood Group'), max_length=5, null=True, blank=True, choices=BG)
    created_at = models.DateTimeField(_('Created'), auto_now_add=True)
    updated_at = models.DateTimeField(_('Updated'), auto_now=True)

    def __str__(self):
        return self.firstname
