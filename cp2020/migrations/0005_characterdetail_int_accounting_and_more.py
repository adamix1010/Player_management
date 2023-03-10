# Generated by Django 4.1.5 on 2023-01-27 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cp2020', '0004_characterdetail_atrr_personal_grooming_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Accounting',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Anthropology',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Awareness',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Biology',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Botany',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Chemistry',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Composition',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Diagnose_Illness',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Education',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Expert',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Gamble',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Geology',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Hide',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_History',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Language_1',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Language_1_Type',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Language_2',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Language_2_Type',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Language_3',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Language_3_Type',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Library_Search',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Mathematics',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Physics',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Programming',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Stock_Market',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_System_Knowledge',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Teaching',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Track',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Wilderness_Survival',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='INT_Zoology',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Archery',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Athletics',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Brawling',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Dance',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Dodge_Escape',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Driving',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Fencing',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Handgun',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Heavy_Weapons',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Martial_Art_1',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Martial_Art_1_Type',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Martial_Art_2',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Martial_Art_2_Type',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Martial_Art_3',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Martial_Art_3_Type',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Melee',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Motorcycle',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Operate_Hvy_Machinery',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Pilot_Dirigible',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Pilot_Fixed_Wing',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Pilot_Gyro',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Pilot_Vect_Thrust',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Rifle',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Stealth',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='REF_Submachinegun',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='TECH_AV_Tech',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='TECH_Aero_Tech',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='TECH_Basic_Tech',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='TECH_Cryotank_Operation',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='TECH_Cyber_Tech',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='TECH_Cyberdeck_Design',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='TECH_Demolitions',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='TECH_Disguise',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='TECH_Elect_Security',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='TECH_Electronics',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='TECH_First_Aid',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='TECH_Forgery',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='TECH_Gyro_Tech',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='TECH_Paint_or_Draw',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='TECH_Pharmacuticals',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='TECH_Photo_Film',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='TECH_Pick_Lock',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='TECH_Play_Instrument',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='TECH_Weaponsmith',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
    ]
