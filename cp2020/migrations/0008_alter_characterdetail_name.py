# Generated by Django 4.1.5 on 2023-01-27 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cp2020', '0007_alter_characterdetail_stat_attr_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characterdetail',
            name='name',
            field=models.TextField(max_length=15),
        ),
    ]
