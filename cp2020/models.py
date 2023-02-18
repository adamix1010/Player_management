from django.db import models
from users.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

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

    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=15)
    role = models.TextField(choices=ROLES, default=SL)
    picture = models.ImageField(upload_to='pictures_storage/',
                                height_field=None,
                                width_field=None,
                                max_length=200,
                                blank=True, null=True)
    stat_INT = models.DecimalField(max_digits=2, decimal_places=0, default=2,
                                    validators=[MinValueValidator(2), MaxValueValidator(10)])
    stat_REF = models.DecimalField(max_digits=2, decimal_places=0, default=2,
                                    validators=[MinValueValidator(2), MaxValueValidator(10)])
    stat_TECH = models.DecimalField(max_digits=2, decimal_places=0, default=2,
                                    validators=[MinValueValidator(2), MaxValueValidator(10)])
    stat_COOL = models.DecimalField(max_digits=2, decimal_places=0, default=2,
                                    validators=[MinValueValidator(2), MaxValueValidator(10)])
    stat_ATTR = models.DecimalField(max_digits=2, decimal_places=0, default=2,
                                    validators=[MinValueValidator(2), MaxValueValidator(10)])
    stat_LUCK = models.DecimalField(max_digits=2, decimal_places=0, default=2,
                                    validators=[MinValueValidator(2), MaxValueValidator(10)])
    stat_MA = models.DecimalField(max_digits=2, decimal_places=0, default=2,
                                    validators=[MinValueValidator(2), MaxValueValidator(10)])
    stat_BODY = models.DecimalField(max_digits=2, decimal_places=0, default=2,
                                    validators=[MinValueValidator(2), MaxValueValidator(10)])
    stat_EMP = models.DecimalField(max_digits=2, decimal_places=0, default=2,
                                    validators=[MinValueValidator(2), MaxValueValidator(10)])
    MA_Run = models.DecimalField(max_digits=3, decimal_places=0,
                                 blank=True, null=True)
    MA_Leap = models.DecimalField(max_digits=3, decimal_places=0,
                                  blank=True, null=True)
    MA_Lift = models.DecimalField(max_digits=3, decimal_places=0,
                                  blank=True, null=True)
    EMP_Humanity = models.DecimalField(max_digits=3, decimal_places=0,
                                       blank=True, null=True)
    BODY_Save_Nr = models.DecimalField(max_digits=3, decimal_places=0,
                                       blank=True, null=True)
    BODY_BTM = models.DecimalField(max_digits=3, decimal_places=0,
                                       blank=True, null=True)

    # Special Skills
    SKILL_Authority = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    SKILL_Char_Leadership = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    SKILL_Combat_Sense = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    SKILL_Credibility = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    SKILL_Family = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    SKILL_Interface = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    SKILL_Jury_Rig = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    SKILL_Medical_Tech = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    SKILL_Resources = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    SKILL_Street_Deal = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    # Atrr Skills
    ATRR_Personal_Grooming = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    ATRR_Wardrobe_Style = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    # Body Skills
    BODY_Endurance = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    BODY_Strength_Feat = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    BODY_Swimming = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    # Cool Skills
    COOL_Interrogation = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    COOL_Intimidate = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    COOL_Oratory = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    COOL_Resist_Torture = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    COOL_Streetwise = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    # Empathy skills
    EMPATHY_Human_Perception = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    EMPATHY_Interview = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    EMPATHY_Leadership = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    EMPATHY_Seduction = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    EMPATHY_Social = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    EMPATHY_Persuasion = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    EMPATHY_Perform = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    # Int skills
    INT_Accounting = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Anthropology = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Awareness = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Biology = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Botany = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Chemistry = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Composition = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Diagnose_Illness = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Education = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Expert = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Gamble = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Geology = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Hide = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_History = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Language_1 = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Language_1_Type = models.CharField(max_length=15, default="")
    INT_Language_2 = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Language_2_Type = models.CharField(max_length=15, default="")
    INT_Language_3 = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Language_3_Type = models.CharField(max_length=15, default="")
    INT_Library_Search = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Mathematics = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Physics = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Programming = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Track = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Stock_Market = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_System_Knowledge = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Teaching = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Wilderness_Survival = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    INT_Zoology = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    # Reflex skills
    REF_Archery = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Athletics = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Brawling = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Dance = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Dodge_Escape = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Driving = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Fencing = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Handgun = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Heavy_Weapons = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Martial_Art_1 = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Martial_Art_1_Type = models.CharField(max_length=15, default="")
    REF_Martial_Art_2 = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Martial_Art_2_Type = models.CharField(max_length=15, default="")
    REF_Martial_Art_3 = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Martial_Art_3_Type = models.CharField(max_length=15, default="")
    REF_Melee = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Motorcycle = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Operate_Hvy_Machinery = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Pilot_Gyro = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Pilot_Fixed_Wing = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Pilot_Dirigible = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Pilot_Vect_Thrust = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Rifle = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Stealth = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    REF_Submachinegun = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    # Tech skills
    TECH_Aero_Tech = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    TECH_AV_Tech = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    TECH_Basic_Tech = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    TECH_Cryotank_Operation = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    TECH_Cyberdeck_Design = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    TECH_Cyber_Tech = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    TECH_Demolitions = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    TECH_Disguise = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    TECH_Electronics = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    TECH_Elect_Security = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    TECH_First_Aid = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    TECH_Forgery = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    TECH_Gyro_Tech = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    TECH_Paint_or_Draw = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    TECH_Photo_Film = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    TECH_Pharmacuticals = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    TECH_Pick_Lock = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    TECH_Play_Instrument = models.DecimalField(max_digits=2, decimal_places=0, default=0)
    TECH_Weaponsmith = models.DecimalField(max_digits=2, decimal_places=0, default=0)

    def __str__(self):
        return f"Character {self.name} belonging to {self.user}"
