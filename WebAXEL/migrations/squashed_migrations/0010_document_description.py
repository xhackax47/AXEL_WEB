# Generated by Django 3.0.1 on 2019-12-29 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAXEL', '0009_auto_20191229_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]