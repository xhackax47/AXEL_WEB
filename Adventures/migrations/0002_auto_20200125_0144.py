# Generated by Django 3.0.2 on 2020-01-25 00:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Adventures', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Objets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default=None, max_length=255, null=True, verbose_name="Nom de l'objet")),
                ('prix', models.IntegerField(blank=True, default=None, null=True, verbose_name="Prix de l'objet")),
                ('poids', models.IntegerField(blank=True, default=None, null=True, verbose_name="Poids de l'objet")),
            ],
        ),
        migrations.CreateModel(
            name='Outils',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(default=None, max_length=255, null=True, verbose_name="Nom de l'outil")),
                ('prix', models.IntegerField(blank=True, default=None, null=True, verbose_name="Prix de l'outil")),
                ('poids', models.IntegerField(blank=True, default=None, null=True, verbose_name="Poids de l'outil")),
            ],
        ),
        migrations.RenameField(
            model_name='character',
            old_name='name',
            new_name='nom',
        ),
        migrations.RenameField(
            model_name='ennemy',
            old_name='name',
            new_name='nom',
        ),
        migrations.RenameField(
            model_name='npc',
            old_name='name',
            new_name='nom',
        ),
        migrations.AddField(
            model_name='arme',
            name='degat',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='arme',
            name='nom',
            field=models.CharField(default=None, max_length=100, verbose_name="Nom de l'arme"),
        ),
        migrations.AddField(
            model_name='arme',
            name='poids',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name="Poids de l'arme en kilogrammes"),
        ),
        migrations.AddField(
            model_name='arme',
            name='proprietes',
            field=models.CharField(blank=True, default=None, max_length=255, null=True, verbose_name="Propriétés de l'arme"),
        ),
        migrations.AddField(
            model_name='armure',
            name='discretion',
            field=models.BooleanField(blank=True, default=None, null=True, verbose_name='Armure discrète ?'),
        ),
        migrations.AddField(
            model_name='armure',
            name='nom',
            field=models.CharField(default=None, max_length=100, verbose_name="Nom de l'armure"),
        ),
        migrations.AddField(
            model_name='bouclier',
            name='ca_bonus',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='CA Bonus'),
        ),
        migrations.AddField(
            model_name='bouclier',
            name='poids',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Poids du bouclier en kilogrammes'),
        ),
        migrations.AddField(
            model_name='npc',
            name='physique',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Adventures.Physique'),
        ),
        migrations.AddField(
            model_name='physique',
            name='categorie_taille',
            field=models.CharField(default=None, max_length=2, verbose_name='Catégorie de taille'),
        ),
        migrations.AlterField(
            model_name='arme',
            name='prix',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name="Prix de l'arme"),
        ),
        migrations.AlterField(
            model_name='armure',
            name='ca_bonus',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='CA Bonus'),
        ),
        migrations.AlterField(
            model_name='armure',
            name='echec_sort',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name="Taux en % de chance d'echecs de sort"),
        ),
        migrations.AlterField(
            model_name='armure',
            name='malus',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Malus Armure'),
        ),
        migrations.AlterField(
            model_name='armure',
            name='max_dex',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Maximum Dextérité'),
        ),
        migrations.AlterField(
            model_name='armure',
            name='poids',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name="Poids de l'armure en livres"),
        ),
        migrations.AlterField(
            model_name='armure',
            name='prix',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name="Prix de l'armure"),
        ),
        migrations.AlterField(
            model_name='bouclier',
            name='prix',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Prix du bouclier'),
        ),
        migrations.AlterField(
            model_name='bourse',
            name='pieces_argent',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name="Pièces d'argent"),
        ),
        migrations.AlterField(
            model_name='bourse',
            name='pieces_cuivre',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Pièces de cuivre'),
        ),
        migrations.AlterField(
            model_name='bourse',
            name='pieces_electrum',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name="Pièces d'électrum"),
        ),
        migrations.AlterField(
            model_name='bourse',
            name='pieces_or',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name="Pièces d'or"),
        ),
        migrations.AlterField(
            model_name='bourse',
            name='pieces_platine',
            field=models.IntegerField(blank=True, default=None, null=True, verbose_name='Pièces de platine'),
        ),
        migrations.AlterField(
            model_name='caracteristiques',
            name='charisme',
            field=models.IntegerField(verbose_name='Charisme'),
        ),
        migrations.AlterField(
            model_name='caracteristiques',
            name='constitution',
            field=models.IntegerField(verbose_name='Constitution'),
        ),
        migrations.AlterField(
            model_name='caracteristiques',
            name='dexterite',
            field=models.IntegerField(verbose_name='Dexterité'),
        ),
        migrations.AlterField(
            model_name='caracteristiques',
            name='force',
            field=models.IntegerField(verbose_name='Force'),
        ),
        migrations.AlterField(
            model_name='caracteristiques',
            name='intelligence',
            field=models.IntegerField(verbose_name='Intelligence'),
        ),
        migrations.AlterField(
            model_name='caracteristiques',
            name='sagesse',
            field=models.IntegerField(verbose_name='Sagesse'),
        ),
        migrations.AlterField(
            model_name='character',
            name='bonus_maitrise',
            field=models.IntegerField(default=None, verbose_name='Bonus de maitrîse'),
        ),
        migrations.AlterField(
            model_name='character',
            name='ca',
            field=models.IntegerField(default=None, verbose_name="Classe d'armure"),
        ),
        migrations.AlterField(
            model_name='character',
            name='caracteristiques',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Adventures.Caracteristiques'),
        ),
        migrations.AlterField(
            model_name='character',
            name='competences',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Adventures.Competences'),
        ),
        migrations.AlterField(
            model_name='character',
            name='equipement',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Adventures.Equipment'),
        ),
        migrations.AlterField(
            model_name='character',
            name='initiative',
            field=models.IntegerField(default=None, verbose_name='Initiative'),
        ),
        migrations.AlterField(
            model_name='character',
            name='level',
            field=models.IntegerField(verbose_name='Niveau'),
        ),
        migrations.AlterField(
            model_name='character',
            name='physique',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Adventures.Physique'),
        ),
        migrations.AlterField(
            model_name='character',
            name='pv_actuels',
            field=models.IntegerField(verbose_name="Points de vie à l'instanté"),
        ),
        migrations.AlterField(
            model_name='character',
            name='pv_temporaires',
            field=models.IntegerField(verbose_name='Points de vie temporaires'),
        ),
        migrations.AlterField(
            model_name='character',
            name='xp',
            field=models.IntegerField(blank=True, default=None, verbose_name='Experience'),
        ),
        migrations.AlterField(
            model_name='competences',
            name='Acrobaties',
            field=models.IntegerField(verbose_name='Acrobaties (DEX)'),
        ),
        migrations.AlterField(
            model_name='competences',
            name='Arcanes',
            field=models.IntegerField(verbose_name='Arcanes (INT)'),
        ),
        migrations.AlterField(
            model_name='competences',
            name='Athletisme',
            field=models.IntegerField(verbose_name='Athletisme (FOR)'),
        ),
        migrations.AlterField(
            model_name='competences',
            name='Discretion',
            field=models.IntegerField(verbose_name='Discretion (DEX)'),
        ),
        migrations.AlterField(
            model_name='competences',
            name='Dressage',
            field=models.IntegerField(verbose_name='Dressage (SAG)'),
        ),
        migrations.AlterField(
            model_name='competences',
            name='Escamotage',
            field=models.IntegerField(verbose_name='Escamotage (DEX)'),
        ),
        migrations.AlterField(
            model_name='competences',
            name='Histoire',
            field=models.IntegerField(verbose_name='Histoire (INT)'),
        ),
        migrations.AlterField(
            model_name='competences',
            name='Intimidation',
            field=models.IntegerField(verbose_name='Intimidation (CHA)'),
        ),
        migrations.AlterField(
            model_name='competences',
            name='Investigation',
            field=models.IntegerField(verbose_name='Investigation (INT)'),
        ),
        migrations.AlterField(
            model_name='competences',
            name='Medecine',
            field=models.IntegerField(verbose_name='Medecine (SAG)'),
        ),
        migrations.AlterField(
            model_name='competences',
            name='Nature',
            field=models.IntegerField(verbose_name='Nature (INT)'),
        ),
        migrations.AlterField(
            model_name='competences',
            name='Perception',
            field=models.IntegerField(verbose_name='Perception (SAG)'),
        ),
        migrations.AlterField(
            model_name='competences',
            name='Perspicacite',
            field=models.IntegerField(verbose_name='Perspicacite (SAG)'),
        ),
        migrations.AlterField(
            model_name='competences',
            name='Persusasion',
            field=models.IntegerField(verbose_name='Persusasion (CHA)'),
        ),
        migrations.AlterField(
            model_name='competences',
            name='Religion',
            field=models.IntegerField(verbose_name='Religion (INT)'),
        ),
        migrations.AlterField(
            model_name='competences',
            name='Representation',
            field=models.IntegerField(verbose_name='Representation (CHA)'),
        ),
        migrations.AlterField(
            model_name='competences',
            name='Survie',
            field=models.IntegerField(verbose_name='Survie (SAG)'),
        ),
        migrations.AlterField(
            model_name='competences',
            name='Tromperie',
            field=models.IntegerField(verbose_name='Tromperie (CHA)'),
        ),
        migrations.AlterField(
            model_name='ennemy',
            name='ca',
            field=models.IntegerField(default=None, verbose_name="Classe d'armure"),
        ),
        migrations.AlterField(
            model_name='ennemy',
            name='level',
            field=models.IntegerField(verbose_name='Niveau'),
        ),
        migrations.AlterField(
            model_name='ennemy',
            name='pv',
            field=models.IntegerField(verbose_name='Points de vie'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='arme',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Adventures.Arme'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='armure',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Adventures.Armure'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='bouclier',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Adventures.Bouclier'),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='bourse',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Adventures.Bourse'),
        ),
        migrations.AlterField(
            model_name='npc',
            name='ca',
            field=models.IntegerField(default=None, verbose_name="Classe d'armure"),
        ),
        migrations.AlterField(
            model_name='npc',
            name='caracteristiques',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Adventures.Caracteristiques'),
        ),
        migrations.AlterField(
            model_name='npc',
            name='competences',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Adventures.Competences'),
        ),
        migrations.AlterField(
            model_name='npc',
            name='equipement',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Adventures.Equipment'),
        ),
        migrations.AlterField(
            model_name='npc',
            name='level',
            field=models.IntegerField(verbose_name='Niveau'),
        ),
        migrations.AlterField(
            model_name='npc',
            name='pv',
            field=models.IntegerField(verbose_name='Points de vie'),
        ),
        migrations.AlterField(
            model_name='physique',
            name='age',
            field=models.IntegerField(verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='physique',
            name='cheveux',
            field=models.IntegerField(verbose_name='Cheveux'),
        ),
        migrations.AlterField(
            model_name='physique',
            name='peau',
            field=models.IntegerField(verbose_name='Peau'),
        ),
        migrations.AlterField(
            model_name='physique',
            name='poids',
            field=models.IntegerField(verbose_name='Poids'),
        ),
        migrations.AlterField(
            model_name='physique',
            name='taille',
            field=models.FloatField(verbose_name='Taille'),
        ),
        migrations.AlterField(
            model_name='physique',
            name='yeux',
            field=models.IntegerField(verbose_name='Yeux'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='objets',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Adventures.Objets'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='outils',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='Adventures.Outils'),
        ),
    ]