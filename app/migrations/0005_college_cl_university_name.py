# Generated by Django 4.0.5 on 2022-07-01 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_remove_collegestaff_cs_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='college',
            name='cl_university_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
