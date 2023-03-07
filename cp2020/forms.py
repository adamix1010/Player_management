from django import forms
from .models import CharacterDetail
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, ButtonHolder
from crispy_forms.bootstrap import TabHolder, Tab


class BasicCharacterInfoForm(forms.ModelForm):
    class Meta:
        model = CharacterDetail
        fields = (
            'name',
            'role',
            'picture',
        )


class BasicCharacterStatsForm(forms.ModelForm):
    class Meta:
        model = CharacterDetail
        fields = (
            'stat_INT',
            'stat_REF',
            'stat_TECH',
            'stat_COOL',
            'stat_ATTR',
            'stat_LUCK',
            'stat_MA',
            'stat_BODY',
            'stat_EMP',
        )


class CharacterSkillForm(forms.ModelForm):
    class Meta:
        model = CharacterDetail

        fields = (
            # Special Skills
            "SKILL_Authority",
            "SKILL_Char_Leadership",
            "SKILL_Combat_Sense",
            "SKILL_Credibility",
            "SKILL_Family",
            "SKILL_Interface",
            "SKILL_Jury_Rig",
            "SKILL_Medical_Tech",
            "SKILL_Resources",
            "SKILL_Street_Deal",
            # Atrr Skills
            "ATRR_Personal_Grooming",
            "ATRR_Wardrobe_Style",
            # Body Skills
            "BODY_Endurance",
            "BODY_Strength_Feat",
            "BODY_Swimming",
            # Cool Skills
            "COOL_Interrogation",
            "COOL_Intimidate",
            "COOL_Oratory",
            "COOL_Resist_Torture",
            "COOL_Streetwise",
            # Empathy skills
            "EMPATHY_Human_Perception",
            "EMPATHY_Interview",
            "EMPATHY_Leadership",
            "EMPATHY_Seduction",
            "EMPATHY_Social",
            "EMPATHY_Persuasion",
            "EMPATHY_Perform",
            # Int skills
            "INT_Accounting",
            "INT_Anthropology",
            "INT_Awareness",
            "INT_Biology",
            "INT_Botany",
            "INT_Chemistry",
            "INT_Composition",
            "INT_Diagnose_Illness",
            "INT_Education",
            "INT_Expert",
            "INT_Gamble",
            "INT_Geology",
            "INT_Hide",
            "INT_History",
            "INT_Language_1",
            "INT_Language_1_Type",
            "INT_Language_2",
            "INT_Language_2_Type",
            "INT_Language_3",
            "INT_Language_3_Type",
            "INT_Library_Search",
            "INT_Mathematics",
            "INT_Physics",
            "INT_Programming",
            "INT_Track",
            "INT_Stock_Market",
            "INT_System_Knowledge",
            "INT_Teaching",
            "INT_Wilderness_Survival",
            "INT_Zoology",
            # Reflex skills
            "REF_Archery",
            "REF_Athletics",
            "REF_Brawling",
            "REF_Dance",
            "REF_Dodge_Escape",
            "REF_Driving",
            "REF_Fencing",
            "REF_Handgun",
            "REF_Heavy_Weapons",
            "REF_Martial_Art_1",
            "REF_Martial_Art_1_Type",
            "REF_Martial_Art_2",
            "REF_Martial_Art_2_Type",
            "REF_Martial_Art_3",
            "REF_Martial_Art_3_Type",
            "REF_Melee",
            "REF_Motorcycle",
            "REF_Operate_Hvy_Machinery",
            "REF_Pilot_Gyro",
            "REF_Pilot_Fixed_Wing",
            "REF_Pilot_Dirigible",
            "REF_Pilot_Vect_Thrust",
            "REF_Rifle",
            "REF_Stealth",
            "REF_Submachinegun",
            # Tech skills
            "TECH_Aero_Tech",
            "TECH_AV_Tech",
            "TECH_Basic_Tech",
            "TECH_Cryotank_Operation",
            "TECH_Cyberdeck_Design",
            "TECH_Cyber_Tech",
            "TECH_Demolitions",
            "TECH_Disguise",
            "TECH_Electronics",
            "TECH_Elect_Security",
            "TECH_First_Aid",
            "TECH_Forgery",
            "TECH_Gyro_Tech",
            "TECH_Paint_or_Draw",
            "TECH_Photo_Film",
            "TECH_Pharmacuticals",
            "TECH_Pick_Lock",
            "TECH_Play_Instrument",
            "TECH_Weaponsmith",

        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            TabHolder(Tab('Special skills',
                          Row(
                              Column('SKILL_Authority', css_class='form-group col-md-2 mb-0'),
                              Column('SKILL_Char_Leadership', css_class='form-group col-md-2 mb-0'),
                              Column("SKILL_Family", css_class='form-group col-md-2 mb-0'),
                              Column("SKILL_Interface", css_class='form-group col-md-2 mb-0'),
                              Column("SKILL_Jury_Rig", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row'
                          ),
                          Row(
                              Column('SKILL_Combat_Sense', css_class='form-group col-md-2 mb-0'),
                              Column('SKILL_Credibility', css_class='form-group col-md-2 mb-0'),
                              Column("SKILL_Medical_Tech", css_class='form-group col-md-2 mb-0'),
                              Column("SKILL_Resources", css_class='form-group col-md-2 mb-0'),
                              Column("SKILL_Street_Deal", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row',

                          )),

                      Tab('Attraction',
                          Row(
                              Column("ATRR_Personal_Grooming", css_class='form-group col-md-2 mb-0'),
                              Column("ATRR_Wardrobe_Style", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row',

                          )),

                      Tab('Body',
                          Row(
                              Column("BODY_Endurance", css_class='form-group col-md-2 mb-0'),
                              Column("BODY_Strength_Feat", css_class='form-group col-md-2 mb-0'),
                              Column("BODY_Swimming", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row',
                          )),

                      Tab('Cool',
                          Row(
                              Column("COOL_Interrogation", css_class='form-group col-md-2 mb-0'),
                              Column("COOL_Intimidate", css_class='form-group col-md-2 mb-0'),
                              Column("COOL_Oratory", css_class='form-group col-md-2 mb-0'),
                              Column("COOL_Resist_Torture", css_class='form-group col-md-2 mb-0'),
                              Column("COOL_Streetwise", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row',
                          )),

                      Tab('Intelligence',
                          Row(
                              Column("INT_Accounting", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Anthropology", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Awareness", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Biology", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Botany", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Chemistry", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row'
                          ),
                          Row(
                              Column("INT_Composition", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Diagnose_Illness", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Education", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Expert", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Gamble", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Geology", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row'
                          ),
                          Row(
                              Column("INT_Hide", css_class='form-group col-md-2 mb-0'),
                              Column("INT_History", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Language_1", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Language_1_Type", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Language_2", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Language_2_Type", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row'
                          ),
                          Row(
                              Column("INT_Language_3", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Language_3_Type", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Library_Search", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Mathematics", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Physics", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Programming", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row'
                          ),
                          Row(
                              Column("INT_Track", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Stock_Market", css_class='form-group col-md-2 mb-0'),
                              Column("INT_System_Knowledge", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Teaching", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Wilderness_Survival", css_class='form-group col-md-2 mb-0'),
                              Column("INT_Zoology", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row'
                          ), ),

                      Tab('Reflex',
                          Row(
                              Column("REF_Archery", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Athletics", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Brawling", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Dance", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Dodge_Escape", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Driving", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row'
                          ),
                          Row(
                              Column("REF_Fencing", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Handgun", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Heavy_Weapons", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Martial_Art_1", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Martial_Art_1_Type", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Martial_Art_2", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row'
                          ),
                          Row(
                              Column("REF_Martial_Art_2_Type", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Martial_Art_3", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Martial_Art_3_Type", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Melee", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Motorcycle", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Operate_Hvy_Machinery", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row'
                          ),
                          Row(
                              Column("REF_Pilot_Gyro", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Pilot_Fixed_Wing", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Pilot_Dirigible", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Pilot_Vect_Thrust", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Rifle", css_class='form-group col-md-2 mb-0'),
                              Column("REF_Stealth", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row'
                          ),
                          Row(
                              Column("REF_Submachinegun", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row',
                          )),
                      Tab('Tech',
                          Row(
                              Column("TECH_Aero_Tech", css_class='form-group col-md-2 mb-0'),
                              Column("TECH_AV_Tech", css_class='form-group col-md-2 mb-0'),
                              Column("TECH_Basic_Tech", css_class='form-group col-md-2 mb-0'),
                              Column("TECH_Cryotank_Operation", css_class='form-group col-md-2 mb-0'),
                              Column("TECH_Cyber_Tech", css_class='form-group col-md-2 mb-0'),
                              Column("TECH_Demolitions", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row',
                          ),
                          Row(
                              Column("TECH_Disguise", css_class='form-group col-md-2 mb-0'),
                              Column("TECH_Electronics", css_class='form-group col-md-2 mb-0'),
                              Column("TECH_Elect_Security", css_class='form-group col-md-2 mb-0'),
                              Column("TECH_First_Aid", css_class='form-group col-md-2 mb-0'),
                              Column("TECH_Forgery", css_class='form-group col-md-2 mb-0'),
                              Column("TECH_Gyro_Tech", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row',
                          ),
                          Row(
                              Column("TECH_Paint_or_Draw", css_class='form-group col-md-2 mb-0'),
                              Column("TECH_Photo_Film", css_class='form-group col-md-2 mb-0'),
                              Column("TECH_Pharmacuticals", css_class='form-group col-md-2 mb-0'),
                              Column("TECH_Pick_Lock", css_class='form-group col-md-2 mb-0'),
                              Column("TECH_Play_Instrument", css_class='form-group col-md-2 mb-0'),
                              Column("TECH_Weaponsmith", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row',
                          ),
                          Row(
                              Column("TECH_Cyberdeck_Design", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row',
                          ),
                          ),
                      Tab('Empathy',
                          Row(
                              Column("EMPATHY_Human_Perception", css_class='form-group col-md-2 mb-0'),
                              Column("EMPATHY_Interview", css_class='form-group col-md-2 mb-0'),
                              Column("EMPATHY_Leadership", css_class='form-group col-md-2 mb-0'),
                              Column("EMPATHY_Seduction", css_class='form-group col-md-2 mb-0'),
                              Column("EMPATHY_Social", css_class='form-group col-md-2 mb-0'),
                              Column("EMPATHY_Persuasion", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row',

                          ),
                          Row(
                              Column("EMPATHY_Perform", css_class='form-group col-md-2 mb-0'),
                              css_class='form-row',

                          )
                          ),
                      ),
            ButtonHolder(
                Submit('save', 'Save'),
            ),
        )
