# Generated by Django 4.0.5 on 2022-08-10 00:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0018_remove_review_rv_ap_id_review_rv_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='rv_cl_id',
            field=models.CharField(default='', max_length=100),
        ),
    ]
