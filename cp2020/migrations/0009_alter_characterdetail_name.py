# Generated by Django 4.1.5 on 2023-01-29 19:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cp2020', '0008_alter_characterdetail_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterdetail',
            name='name',
            field=models.CharField(max_length=15),
        ),
    ]
