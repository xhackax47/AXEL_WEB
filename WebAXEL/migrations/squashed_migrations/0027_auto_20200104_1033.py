# Generated by Django 3.0.1 on 2020-01-04 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAXEL', '0026_auto_20200104_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='axeluser',
            name='email',
            field=models.EmailField(default='', max_length=254, unique=True, verbose_name='email address'),
        ),
    ]
