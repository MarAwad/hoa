# Generated by Django 4.0.10 on 2023-07-20 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contractrequests', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contractrequest',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
