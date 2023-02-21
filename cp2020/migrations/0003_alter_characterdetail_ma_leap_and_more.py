# Generated by Django 4.1.5 on 2023-01-21 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cp2020', '0002_characterdetail_delete_characterdetails'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterdetail',
            name='MA_Leap',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='characterdetail',
            name='MA_Lift',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='characterdetail',
            name='MA_Run',
            field=models.DecimalField(blank=True, decimal_places=0, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='characterdetail',
            name='picture',
            field=models.ImageField(blank=True, max_length=200, null=True, upload_to='pictures_storage/'),
        ),
    ]
