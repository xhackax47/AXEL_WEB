# Generated by Django 3.0.1 on 2020-01-07 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WebAXEL', '0046_auto_20200107_1358'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='categories_dataset',
        ),
        migrations.AddField(
            model_name='dataset',
            name='categories_dataset',
            field=models.ManyToManyField(blank=True, default=None, to='WebAXEL.DataSetCategory', verbose_name="Catégorie de l'ensemble de données"),
        ),
    ]
