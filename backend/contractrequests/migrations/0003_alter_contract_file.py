# Generated by Django 4.0.10 on 2023-07-21 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractrequests', '0002_contractrequest_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contract',
            name='file',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
