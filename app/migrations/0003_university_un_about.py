# Generated by Django 4.0.5 on 2022-06-30 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_college_collegerequest_collegestaff_courses_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='university',
            name='un_about',
            field=models.CharField(default='', max_length=100),
        ),
    ]
