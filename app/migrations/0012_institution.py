# Generated by Django 4.0.5 on 2022-07-17 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_collegerequest_cr_seat_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('in_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('in_image', models.FileField(upload_to='app/static/media/images')),
                ('in_name', models.CharField(max_length=100)),
                ('in_mobile', models.CharField(max_length=100)),
                ('in_email', models.CharField(max_length=100)),
                ('in_address', models.CharField(max_length=100)),
                ('in_about', models.CharField(max_length=100)),
                ('in_status', models.IntegerField(default=0)),
                ('in_created_by', models.CharField(max_length=100)),
            ],
        ),
    ]
