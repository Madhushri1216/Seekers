# Generated by Django 4.0.5 on 2022-08-09 23:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rv_ap_id',
        ),
        migrations.AddField(
            model_name='review',
            name='rv_created_by',
            field=models.CharField(default='', max_length=100),
        ),
    ]
