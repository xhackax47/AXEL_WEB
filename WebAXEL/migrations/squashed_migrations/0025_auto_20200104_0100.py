# Generated by Django 3.0.1 on 2020-01-04 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WebAXEL', '0024_auto_20200104_0058'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='axeluser',
            options={},
        ),
        migrations.AlterModelManagers(
            name='axeluser',
            managers=[
            ],
        ),
        migrations.RemoveField(
            model_name='axeluser',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='axeluser',
            name='email',
        ),
        migrations.RemoveField(
            model_name='axeluser',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='axeluser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='axeluser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='axeluser',
            name='is_staff',
        ),
        migrations.RemoveField(
            model_name='axeluser',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='axeluser',
            name='last_name',
        ),
        migrations.RemoveField(
            model_name='axeluser',
            name='user_permissions',
        ),
    ]
