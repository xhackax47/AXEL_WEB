# Generated by Django 3.0.1 on 2019-12-30 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAXEL', '0011_auto_20191229_1513'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='document',
            field=models.FileField(null=True, upload_to='static/docs'),
        ),
    ]
