# Generated by Django 3.0.1 on 2020-01-07 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('WebAXEL', '0045_auto_20200107_1314'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='dataset',
            name='categories_dataset',
        ),
        migrations.AddField(
            model_name='dataset',
            name='categories_dataset',
            field=models.OneToOneField(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='WebAXEL.DataSetCategory', verbose_name="Catégorie de l'ensemble de données"),
        ),
    ]