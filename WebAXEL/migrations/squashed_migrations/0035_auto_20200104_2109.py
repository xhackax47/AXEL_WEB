# Generated by Django 3.0.1 on 2020-01-04 20:09

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
        ('WebAXEL', '0034_customgroup'),
    ]

    operations = [
        migrations.CreateModel(
            name='AxelGroup',
            fields=[
                ('group_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.Group')),
                ('description', models.CharField(max_length=1024)),
            ],
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.DeleteModel(
            name='CustomGroup',
        ),
    ]
