# Generated by Django 3.0.1 on 2020-01-06 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAXEL', '0036_auto_20200106_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='axeluser',
            name='profile_img',
            field=models.ImageField(blank=True, upload_to='static/img/profilesImages/'),
        ),
    ]
