# Generated by Django 4.1.5 on 2023-01-25 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cp2020', '0003_alter_characterdetail_ma_leap_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='characterdetail',
            name='ATRR_Personal_Grooming',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='ATRR_Wardrobe_Style',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='BODY_Endurance',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='BODY_Strength_Feat',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='BODY_Swimming',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='COOL_Interrogation',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='COOL_Intimidate',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='COOL_Oratory',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='COOL_Resist_Torture',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='COOL_Streetwise',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='EMPATHY_Human_Perception',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='EMPATHY_Interview',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='EMPATHY_Leadership',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='EMPATHY_Perform',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='EMPATHY_Persuasion',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='EMPATHY_Seduction',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='EMPATHY_Social',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='SKILL_Authority',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='SKILL_Char_Leadership',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='SKILL_Combat_Sense',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='SKILL_Credibility',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='SKILL_Family',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='SKILL_Interface',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='SKILL_Jury_Rig',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='SKILL_Medical_Tech',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='SKILL_Resources',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
        migrations.AddField(
            model_name='characterdetail',
            name='SKILL_Street_Deal',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=2),
        ),
    ]
