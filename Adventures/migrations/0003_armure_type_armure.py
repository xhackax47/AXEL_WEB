# Generated by Django 3.0.2 on 2020-01-25 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adventures', '0002_auto_20200125_0144'),
    ]

    operations = [
        migrations.AddField(
            model_name='armure',
            name='type_armure',
            field=models.CharField(default=None, max_length=100, verbose_name="Type de l'armure"),
        ),
    ]