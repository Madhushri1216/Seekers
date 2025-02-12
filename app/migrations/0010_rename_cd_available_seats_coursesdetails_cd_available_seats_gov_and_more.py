# Generated by Django 4.0.5 on 2022-07-08 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_collegerequest_cr_amount'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coursesdetails',
            old_name='cd_available_seats',
            new_name='cd_available_seats_gov',
        ),
        migrations.RemoveField(
            model_name='coursesdetails',
            name='cd_total_seats',
        ),
        migrations.AddField(
            model_name='coursesdetails',
            name='cd_available_seats_mng',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='coursesdetails',
            name='cd_total_seats_gov',
            field=models.CharField(default=0, max_length=100),
        ),
        migrations.AddField(
            model_name='coursesdetails',
            name='cd_total_seats_mng',
            field=models.CharField(default=0, max_length=100),
        ),
    ]
