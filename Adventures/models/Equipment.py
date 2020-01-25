from django.db import models
from django.db.models import Model, IntegerField, ForeignKey, FloatField, CharField, BooleanField
from django.utils.translation import ugettext_lazy as _


class Armure(Model):
    nom = CharField(max_length=100,verbose_name="Nom de l'armure", default=None)
    prix = IntegerField(blank=True, null=True, default=None,
                        verbose_name=_("Prix de l'armure"))
    ca_bonus = IntegerField(blank=True, null=True, default=None, verbose_name=_("CA Bonus"))
    max_dex = IntegerField(blank=True, null=True, default=None, verbose_name=_("Maximum Dextérité"))
    malus = IntegerField(blank=True, null=True, default=None, verbose_name=_("Malus Armure"))
    echec_sort = IntegerField(blank=True, null=True, default=None,
                              verbose_name=_("Taux en % de chance d'echecs de sort"))
    vitesse_deplacement = FloatField(max_length=2, blank=True, null=True, default=None,
                                     verbose_name=_("Vitesse Déplacement avec armure"))
    poids = IntegerField(blank=True, null=True, default=None,
                         verbose_name=_("Poids de l'armure en livres"))
    discretion = BooleanField(blank=True, null=True, default=None, verbose_name=_("Armure discrète ?"))


class Arme(Model):
    nom = CharField(max_length=100,verbose_name="Nom de l'arme", default=None)
    prix = IntegerField(blank=True, null=True, default=None,
                        verbose_name=_("Prix de l'arme"))
    degat = IntegerField(null=False, blank=False, default=1)
    poids = IntegerField(blank=True, null=True, default=None,
                         verbose_name=_("Poids de l'arme en kilogrammes"))
    proprietes = CharField(max_length=255,blank=True, null=True, default=None, verbose_name=_("Propriétés de l'arme"))


class Bouclier(Model):
    prix = IntegerField(blank=True, null=True, default=None,
                        verbose_name=_("Prix du bouclier"))
    ca_bonus = IntegerField(blank=True, null=True, default=None, verbose_name=_("CA Bonus"))
    poids = IntegerField(blank=True, null=True, default=None,
                         verbose_name=_("Poids du bouclier en kilogrammes"))


class Bourse(Model):
    pieces_platine = IntegerField(blank=True, null=True, default=None,
                                  verbose_name=_("Pièces de platine"))
    pieces_or = IntegerField(blank=True, null=True, default=None, verbose_name=_("Pièces d'or"))
    pieces_electrum = IntegerField(blank=True, null=True, default=None,
                                   verbose_name=_("Pièces d'électrum"))
    pieces_argent = IntegerField(blank=True, null=True, default=None, verbose_name=_("Pièces d'argent"))
    pieces_cuivre = IntegerField(blank=True, null=True, default=None, verbose_name=_("Pièces de cuivre"))


class Objets(Model):
    nom = CharField(max_length=255,verbose_name="Nom de l'objet", null=True, default=None)
    prix = IntegerField(blank=True, null=True, default=None,
                        verbose_name=_("Prix de l'objet"))
    poids = IntegerField(blank=True, null=True, default=None,
                         verbose_name=_("Poids de l'objet"))


class Outils(Model):
    nom = CharField(max_length=255,verbose_name="Nom de l'outil", null=True, default=None)
    prix = IntegerField(blank=True, null=True, default=None,
                        verbose_name=_("Prix de l'outil"))
    poids = IntegerField(blank=True, null=True, default=None,
                         verbose_name=_("Poids de l'outil"))


class Equipment(Model):
    armure = ForeignKey(Armure, on_delete=models.CASCADE, default=None)
    arme = ForeignKey(Arme, on_delete=models.CASCADE, default=None)
    bouclier = ForeignKey(Bouclier, on_delete=models.CASCADE, default=None)
    bourse = ForeignKey(Bourse, on_delete=models.CASCADE, default=None)
    objets = ForeignKey(Objets, on_delete=models.CASCADE, default=None)
    outils = ForeignKey(Outils, on_delete=models.CASCADE, default=None)
