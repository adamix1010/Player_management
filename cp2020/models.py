from django.db import models
from users.models import User


class CharacterDetail(models.Model):
    SL = 'SOLO'
    RC = 'ROCKER'
    NR = "NETRUNNER"
    MD = "MEDIA"
    ND = "NOMAD"
    FX = "FIXER"
    CP = "COP"
    CR = "CORP"
    TC = "TECHIE"
    MC = "MEDTECHIE"

    ROLES = [
        (SL, "Solo"),
        (RC, "Rocker"),
        (NR, "Netrunner"),
        (MD, "Media"),
        (ND, "Nomad"),
        (FX, "Fixer"),
        (CP, "Cop"),
        (CR, "Corp"),
        (TC, "Techie"),
        (MC, "Medtechie"),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.TextField(max_length=50)
    role = models.TextField(choices=ROLES, default=SL)
    picture = models.ImageField(upload_to='pictures_storage/', height_field=None, width_field=None, max_length=200, blank=True, null=True)
    stat_INT = models.DecimalField(max_digits=2, decimal_places=0)
    stat_REF = models.DecimalField(max_digits=2, decimal_places=0)
    stat_TECH = models.DecimalField(max_digits=2, decimal_places=0)
    stat_INT = models.DecimalField(max_digits=2, decimal_places=0)
    stat_COOL = models.DecimalField(max_digits=2, decimal_places=0)
    stat_ATTR = models.DecimalField(max_digits=2, decimal_places=0)
    stat_LUCK = models.DecimalField(max_digits=2, decimal_places=0)
    stat_MA = models.DecimalField(max_digits=2, decimal_places=0)
    stat_BODY = models.DecimalField(max_digits=2, decimal_places=0)
    stat_EMP = models.DecimalField(max_digits=2, decimal_places=0)
    stat_ATTR = models.DecimalField(max_digits=2, decimal_places=0)
    MA_Run = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    MA_Leap = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    MA_Lift = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    def __str__(self):
        return f"Character {self.name} belonging to {self.user}"

