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
    picture = models.ImageField(upload_to='pictures_storage/', height_field=None, width_field=None, max_length=200,)

    def __str__(self):
        return f"Character {self.name} belonging to {self.user}"

